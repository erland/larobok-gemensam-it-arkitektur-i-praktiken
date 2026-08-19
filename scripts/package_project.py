#!/usr/bin/env python3
from __future__ import annotations
import argparse
from pathlib import Path
import zipfile

EXCLUDED_PARTS = {'.git', '__pycache__', '__MACOSX'}
EXCLUDED_NAMES = {'.DS_Store'}

def include(path: Path, root: Path) -> bool:
    rel = path.relative_to(root)
    if any(part in EXCLUDED_PARTS for part in rel.parts):
        return False
    if path.name in EXCLUDED_NAMES or path.suffix == '.pyc':
        return False
    return path.is_file()

def main() -> int:
    ap = argparse.ArgumentParser(description='Paketera bokprojekt utan lokala arbetsfiler.')
    ap.add_argument('root', nargs='?', default='.')
    ap.add_argument('--output', required=True)
    args = ap.parse_args()
    root = Path(args.root).resolve()
    out = Path(args.output).resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    if out.exists():
        out.unlink()
    files = [p for p in sorted(root.rglob('*')) if include(p, root) and p.resolve() != out]
    with zipfile.ZipFile(out, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for p in files:
            zf.write(p, p.relative_to(root).as_posix())
    print(f'OK: skapade {out} med {len(files)} filer; .git och lokala arbetsfiler exkluderade.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
