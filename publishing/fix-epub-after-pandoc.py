#!/usr/bin/env python3
from __future__ import annotations
import re, sys, tempfile, zipfile
from pathlib import Path
from xml.etree import ElementTree as ET
OPF="http://www.idpf.org/2007/opf"; XHTML="http://www.w3.org/1999/xhtml"; EPUB="http://www.idpf.org/2007/ops"
NS={"opf":OPF,"x":XHTML,"epub":EPUB}


def rootfile(base: Path) -> Path:
    tree=ET.parse(base/'META-INF/container.xml')
    node=tree.find('.//{urn:oasis:names:tc:opendocument:xmlns:container}rootfile')
    if node is None: raise RuntimeError('EPUB container saknar rootfile')
    return Path(node.attrib['full-path'])


def split_headings(base: Path)->tuple[int,int]:
    chapters=0; parts=0
    chapter_pat=re.compile(r'^\s*(\d+)\.\s+(.+?)\s*$')
    part_pat=re.compile(r'^\s*Del\s+([IVX]+)\s+[–-]\s+(.+?)\s*$', re.I)
    for path in base.rglob('*.xhtml'):
        tree=ET.parse(path); changed=False
        root=tree.getroot()
        body=root.find('.//x:body',NS)
        for h1 in root.findall('.//x:h1',NS):
            text=''.join(h1.itertext()).strip()
            pm=part_pat.match(text)
            if pm:
                ident=h1.attrib.get('id'); h1.clear()
                if ident: h1.set('id',ident)
                h1.set('class','part-heading')
                a=ET.SubElement(h1,f'{{{XHTML}}}span',{'class':'part-number'}); a.text=f'Del {pm.group(1).upper()}'
                b=ET.SubElement(h1,f'{{{XHTML}}}span',{'class':'part-title'}); b.text=pm.group(2)
                if body is not None:
                    existing=body.attrib.get('class','').split()
                    if 'part-page' not in existing: body.set('class',' '.join(existing+['part-page']).strip())
                changed=True; parts+=1; continue
            m=chapter_pat.match(text)
            if not m: continue
            ident=h1.attrib.get('id'); h1.clear()
            if ident: h1.set('id',ident)
            a=ET.SubElement(h1,f'{{{XHTML}}}span',{'class':'chapter-number'}); a.text=m.group(1)
            b=ET.SubElement(h1,f'{{{XHTML}}}span',{'class':'chapter-title'}); b.text=m.group(2)
            changed=True; chapters+=1
        if changed: tree.write(path,encoding='utf-8',xml_declaration=True)
    return chapters,parts


def _label_from_markup(fragment: str) -> str:
    import html
    return html.unescape(re.sub(r'<[^>]+>', '', fragment)).strip()


def group_nav_by_parts(base: Path)->int:
    """Group Pandoc's flat EPUB3 TOC without reserializing its XML namespaces.

    Some readers are stricter than the XML standard and have problems with nav.xhtml
    after ElementTree rewrites the default XHTML/epub namespaces to generated prefixes.
    Pandoc's original serialization is therefore preserved byte-for-byte except for
    the <ol class="toc"> contents that we intentionally nest.
    """
    path=base/'EPUB/nav.xhtml'
    if not path.is_file():
        candidates=list(base.rglob('nav.xhtml'))
        if not candidates: raise RuntimeError('EPUB saknar nav.xhtml')
        path=candidates[0]
    text=path.read_text(encoding='utf-8')
    m=re.search(r'(<nav\s+epub:type="toc"[^>]*>.*?<ol\s+class="toc">)(.*?)(</ol>\s*</nav>)', text, re.S)
    if not m: raise RuntimeError('EPUB nav.xhtml saknar förväntad TOC-struktur')
    body=m.group(2)
    items=re.findall(r'<li\b[^>]*>.*?</li>', body, re.S)
    if not items: raise RuntimeError('EPUB nav.xhtml innehåller inga TOC-poster')
    out=[]; grouped=0; current_part=None; children=[]
    def flush_part():
        nonlocal current_part, children
        if current_part is not None:
            if children:
                out.append(current_part[:-5] + '<ol>' + ''.join(children) + '</ol></li>')
            else:
                out.append(current_part)
        current_part=None; children=[]
    for li in items:
        am=re.search(r'<a\b[^>]*>(.*?)</a>', li, re.S)
        label=_label_from_markup(am.group(1)) if am else ''
        if re.match(r'^Del\s+[IVX]+\s+[–-]\s+',label,re.I):
            flush_part(); current_part=li; continue
        if re.match(r'^\d+\.\s+',label) and current_part is not None:
            children.append(li); grouped+=1; continue
        flush_part(); out.append(li)
    flush_part()
    new_text=text[:m.start(2)] + ''.join(out) + text[m.end(2):]
    path.write_text(new_text,encoding='utf-8')
    return grouped


def group_ncx_by_parts(base: Path)->int:
    """Group the legacy NCX while preserving Pandoc's default namespace syntax."""
    path=base/'EPUB/toc.ncx'
    if not path.is_file():
        candidates=list(base.rglob('*.ncx'))
        if not candidates: return 0
        path=candidates[0]
    text=path.read_text(encoding='utf-8')
    m=re.search(r'(<navMap>)(.*?)(</navMap>)', text, re.S)
    if not m: raise RuntimeError('EPUB NCX saknar navMap')
    body=m.group(2)
    items=re.findall(r'<navPoint\b[^>]*>.*?</navPoint>', body, re.S)
    if not items: return 0
    out=[]; grouped=0; current_part_index=None
    for item in items:
        lm=re.search(r'<navLabel>\s*<text>(.*?)</text>\s*</navLabel>',item,re.S)
        label=_label_from_markup(lm.group(1)) if lm else ''
        if re.match(r'^Del\s+[IVX]+\s+[–-]\s+',label,re.I):
            out.append(item); current_part_index=len(out)-1; continue
        if re.match(r'^\d+\.\s+',label) and current_part_index is not None:
            parent=out[current_part_index]
            parent=parent[:-len('</navPoint>')] + item + '</navPoint>'
            out[current_part_index]=parent; grouped+=1
        else:
            out.append(item)
            if not re.match(r'^\d+\.\s+',label): current_part_index=None
    new_text=text[:m.start(2)] + ''.join(out) + text[m.end(2):]
    new_text=re.sub(r'(<meta\s+name="dtb:depth"\s+content=")[^"]*("\s*/>)',r'\g<1>2\2',new_text,count=1)
    path.write_text(new_text,encoding='utf-8')
    return grouped


def nav_non_linear(base: Path, opf_rel: Path)->bool:
    """Mark the navigation document non-linear without rewriting OPF namespaces."""
    path=base/opf_rel
    text=path.read_text(encoding='utf-8')
    nav_item=re.search(r'<item\b(?=[^>]*\bproperties="[^"]*\bnav\b[^"]*")(?=[^>]*\bid="([^"]+)")[^>]*/>',text)
    if not nav_item:
        nav_item=re.search(r'<item\b(?=[^>]*\bid="([^"]+)")(?=[^>]*\bproperties="[^"]*\bnav\b[^"]*")[^>]*/>',text)
    if not nav_item: raise RuntimeError('EPUB OPF saknar nav-item')
    nav_id=nav_item.group(1)
    pat=re.compile(r'(<itemref\b[^>]*\bidref="'+re.escape(nav_id)+r'"[^>]*)(/>)')
    mm=pat.search(text)
    if not mm: raise RuntimeError('EPUB OPF spine saknar nav-itemref')
    if re.search(r'\blinear="no"',mm.group(1)): return False
    repl=mm.group(1)+' linear="no"'+mm.group(2)
    path.write_text(text[:mm.start()]+repl+text[mm.end():],encoding='utf-8')
    return True


def validate_navigation(base: Path)->None:
    nav_candidates=list(base.rglob('nav.xhtml'))
    if not nav_candidates: raise RuntimeError('EPUB-validering: nav.xhtml saknas')
    text=nav_candidates[0].read_text(encoding='utf-8')
    if 'xmlns="http://www.w3.org/1999/xhtml"' not in text or 'xmlns:epub="http://www.idpf.org/2007/ops"' not in text:
        raise RuntimeError('EPUB-validering: Pandocs standard-namespace i nav.xhtml har ändrats')
    if '<html:' in text or 'ns1:type=' in text:
        raise RuntimeError('EPUB-validering: genererade XML-prefix finns kvar i nav.xhtml')
    part_count=len(re.findall(r'<li\b[^>]*><a\b[^>]*>Del\s+[IVX]+\s+[–-]\s+',text,re.I))
    chapter_count=len(re.findall(r'<li\b[^>]*><a\b[^>]*>\d+\.\s+',text))
    nested_count=len(re.findall(r'Del\s+[IVX]+\s+[–-].*?<ol>.*?<li\b[^>]*><a\b[^>]*>\d+\.\s+',text,re.I|re.S))
    if part_count!=6 or chapter_count!=37 or nested_count<6:
        raise RuntimeError(f'EPUB-validering: oväntad TOC-struktur (delar={part_count}, kapitel={chapter_count}, grupper={nested_count})')
    for href in re.findall(r'<a\b[^>]*href="([^"]+)"',text):
        file_part=href.split('#',1)[0]
        if not file_part: continue
        target=(nav_candidates[0].parent/file_part).resolve()
        if not target.is_file(): raise RuntimeError('EPUB-validering: TOC-länk saknar mål: '+href)

def repack(base:Path,out:Path)->None:
    if out.exists(): out.unlink()
    with zipfile.ZipFile(out,'w') as z:
        mime=base/'mimetype'; z.write(mime,'mimetype',compress_type=zipfile.ZIP_STORED)
        for p in sorted(base.rglob('*')):
            if p.is_file() and p!=mime: z.write(p,p.relative_to(base).as_posix(),compress_type=zipfile.ZIP_DEFLATED)


def validate(path:Path)->None:
    with zipfile.ZipFile(path) as z:
        if not z.namelist() or z.namelist()[0]!='mimetype' or z.getinfo('mimetype').compress_type!=zipfile.ZIP_STORED:
            raise RuntimeError('EPUB-fel: mimetype måste ligga först och vara okomprimerad')
        if 'META-INF/container.xml' not in z.namelist(): raise RuntimeError('EPUB-fel: container.xml saknas')


def main()->int:
    if len(sys.argv)!=2: print('Användning: fix-epub-after-pandoc.py <fil.epub>',file=sys.stderr); return 2
    epub=Path(sys.argv[1]).resolve()
    with tempfile.TemporaryDirectory(prefix='fix-epub-') as td:
        base=Path(td)
        with zipfile.ZipFile(epub) as z: z.extractall(base)
        opf=rootfile(base)
        chapters,parts=split_headings(base)
        grouped=group_nav_by_parts(base)
        ncx_grouped=group_ncx_by_parts(base)
        nav=nav_non_linear(base,opf)
        validate_navigation(base)
        repack(base,epub)
    validate(epub)
    print(f'Efterbearbetad EPUB: kapitelfiler={chapters}, delsidor={parts}, grupperade TOC-kapitel={grouped}, NCX-kapitel={ncx_grouped}, nav linear=no={nav}')
    return 0
if __name__=='__main__': raise SystemExit(main())
