#!/usr/bin/env python3
import re, sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
errors = []
skills = sorted(p for p in (root / "skills").iterdir() if p.is_dir())
for d in skills:
    f = d / "SKILL.md"
    if not f.exists():
        errors.append(f"{d.name}: missing SKILL.md")
        continue
    m = re.match(r"---\n(.*?)\n---\n", f.read_text(), re.S)
    if not m:
        errors.append(f"{d.name}: missing frontmatter")
        continue
    fm = dict(l.split(": ", 1) for l in m.group(1).splitlines() if ": " in l)
    if fm.get("name") != d.name:
        errors.append(f"{d.name}: name must match directory")
    if not fm.get("description"):
        errors.append(f"{d.name}: missing description")
manifest = (root / "projection.omni.yaml").read_text()
for d in skills:
    if f"source: skills/{d.name}\n" not in manifest:
        errors.append(f"{d.name}: not listed in projection.omni.yaml")
for e in errors:
    print(e)
sys.exit(1 if errors else 0)
