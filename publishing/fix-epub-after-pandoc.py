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


def group_nav_by_parts(base: Path)->int:
    grouped=0
    for path in base.rglob('*.xhtml'):
        tree=ET.parse(path); root=tree.getroot()
        navs=root.findall('.//x:nav',NS)
        changed=False
        for nav in navs:
            typ=nav.attrib.get(f'{{{EPUB}}}type','')
            if typ!='toc': continue
            ol=nav.find('x:ol',NS)
            if ol is None: continue
            items=list(ol.findall('x:li',NS))
            current_part=None
            for li in items:
                a=li.find('x:a',NS)
                label=''.join(a.itertext()).strip() if a is not None else ''
                if re.match(r'^Del\s+[IVX]+\s+[–-]\s+',label,re.I):
                    current_part=li
                    continue
                if re.match(r'^\d+\.\s+',label) and current_part is not None:
                    sub=current_part.find('x:ol',NS)
                    if sub is None: sub=ET.SubElement(current_part,f'{{{XHTML}}}ol')
                    ol.remove(li); sub.append(li); grouped+=1; changed=True
                elif not re.match(r'^\d+\.\s+',label):
                    current_part=None
        if changed: tree.write(path,encoding='utf-8',xml_declaration=True)
    return grouped



def group_ncx_by_parts(base: Path)->int:
    ns='http://www.daisy.org/z3986/2005/ncx/'
    grouped=0
    for path in base.rglob('*.ncx'):
        tree=ET.parse(path); root=tree.getroot()
        navmap=root.find(f'{{{ns}}}navMap')
        if navmap is None: continue
        items=list(navmap.findall(f'{{{ns}}}navPoint'))
        current_part=None; changed=False
        for item in items:
            text_node=item.find(f'{{{ns}}}navLabel/{{{ns}}}text')
            label=(text_node.text or '').strip() if text_node is not None else ''
            if re.match(r'^Del\s+[IVX]+\s+[–-]\s+',label,re.I):
                current_part=item
                continue
            if re.match(r'^\d+\.\s+',label) and current_part is not None:
                navmap.remove(item); current_part.append(item); grouped+=1; changed=True
            elif not re.match(r'^\d+\.\s+',label):
                current_part=None
        if changed:
            depth=root.find(f'{{{ns}}}head/{{{ns}}}meta[@name="dtb:depth"]')
            if depth is not None: depth.set('content','2')
            tree.write(path,encoding='utf-8',xml_declaration=True)
    return grouped

def nav_non_linear(base: Path, opf_rel: Path)->bool:
    path=base/opf_rel; tree=ET.parse(path); manifest=tree.getroot().find('opf:manifest',NS); spine=tree.getroot().find('opf:spine',NS)
    if manifest is None or spine is None: raise RuntimeError('EPUB OPF saknar manifest/spine')
    nav_ids={i.attrib['id'] for i in manifest.findall('opf:item',NS) if 'nav' in i.attrib.get('properties','').split()}
    changed=False
    for item in spine.findall('opf:itemref',NS):
        if item.attrib.get('idref') in nav_ids and item.attrib.get('linear')!='no': item.set('linear','no'); changed=True
    if changed: tree.write(path,encoding='utf-8',xml_declaration=True)
    return changed


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
        repack(base,epub)
    validate(epub)
    print(f'Efterbearbetad EPUB: kapitelfiler={chapters}, delsidor={parts}, grupperade TOC-kapitel={grouped}, NCX-kapitel={ncx_grouped}, nav linear=no={nav}')
    return 0
if __name__=='__main__': raise SystemExit(main())
