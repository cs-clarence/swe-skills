#!/usr/bin/env python3
"""Validate skills, the omni projection manifest, and references into swe-docs.

Usage: python3 scripts/validate_skills.py --guidelines <path to swe-docs docs/guidelines> [--schema <projection schema json>]
"""
import argparse, json, re, sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
MAX_LINES = 200
errors = []


def err(msg):
    errors.append(msg)


def heading_slugs(path):
    text = re.sub(r"^```.*?^```", "", path.read_text(encoding="utf-8"), flags=re.S | re.M)
    seen, slugs = {}, set()
    for h in re.findall(r"^#+[ \t]+(.*)$", text, re.M):
        base = re.sub(r"[ \t]", "-", re.sub(r"[^\w \t-]", "", h.lower().strip()))
        n = seen.get(base, 0)
        seen[base] = n + 1
        slugs.add(base if n == 0 else f"{base}-{n}")
    return slugs


def check_skill(d, guidelines):
    f = d / "SKILL.md"
    if not f.exists():
        return err(f"{d.name}: missing SKILL.md")
    text = f.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n(.*)", text, re.S)
    if not m:
        return err(f"{d.name}: missing frontmatter")
    try:
        fm = yaml.safe_load(m.group(1))
    except yaml.YAMLError as e:
        return err(f"{d.name}: invalid frontmatter: {e}")
    if not isinstance(fm, dict):
        return err(f"{d.name}: frontmatter must be a mapping")
    extra = set(fm) - {"name", "description"}
    if extra:
        err(f"{d.name}: unknown frontmatter keys {sorted(extra)}")
    name, desc = fm.get("name"), fm.get("description")
    if name != d.name:
        err(f"{d.name}: name must match directory")
    if not isinstance(name, str) or not NAME_RE.match(name) or len(name) > 64:
        err(f"{d.name}: name must be kebab-case, at most 64 chars")
    if not isinstance(desc, str) or not desc.strip():
        err(f"{d.name}: missing description")
    else:
        if len(desc) > 1024:
            err(f"{d.name}: description over 1024 chars")
        if not re.search(r"\bUse (when|for|after|before)\b", desc):
            err(f"{d.name}: description must say when to use the skill ('Use when ...')")
    body = m.group(2)
    if len(text.splitlines()) > MAX_LINES:
        err(f"{d.name}: SKILL.md over {MAX_LINES} lines")
    if not body.lstrip().startswith("# "):
        err(f"{d.name}: body must start with a '# ' title")
    if "docs/guidelines" not in body:
        err(f"{d.name}: must reference docs/guidelines")
    for n in re.findall(r"\bswe-[a-z-]+\b", body):
        if not (ROOT / "skills" / n).is_dir() and n not in {"swe-docs", "swe-skills"}:
            err(f"{d.name}: references unknown skill {n}")
    for ref in set(re.findall(r"`([^`\s]+)`", body)):
        rel, _, anchor = ref.removeprefix("docs/guidelines").lstrip("/").partition("#")
        if not re.match(r"(core|planning|authoring|reviewing)/|README\.md$|CHANGELOG\.md$", rel) and rel:
            continue
        if not (guidelines / rel).exists():
            err(f"{d.name}: `{ref}` does not exist in swe-docs")
        elif anchor and anchor not in heading_slugs(guidelines / rel):
            err(f"{d.name}: `{ref}` heading does not exist in swe-docs")


def check_manifest(skills, schema):
    path = ROOT / "projection.omni.yaml"
    manifest = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(manifest, dict):
        return err("projection.omni.yaml: must be a mapping")
    if schema:
        import jsonschema
        for e in jsonschema.Draft202012Validator(json.loads(Path(schema).read_text(encoding="utf-8"))).iter_errors(manifest):
            err(f"projection.omni.yaml: {'/'.join(map(str, e.absolute_path))}: {e.message}")
    rules = []
    for route in manifest.get("routes") or []:
        rules.extend(route.get("rules") or [])
    for r in rules:
        if not isinstance(r, dict) or not r.get("source") or not r.get("dest"):
            err(f"projection.omni.yaml: rule needs source and dest: {r}")
    rules = [r for r in rules if isinstance(r, dict) and r.get("source") and r.get("dest")]
    sources = [r["source"] for r in rules]
    dests = [r["dest"] for r in rules]
    for dup in {x for x in dests if dests.count(x) > 1}:
        err(f"projection.omni.yaml: duplicate dest {dup}")
    for s in sources:
        if not (ROOT / s / "SKILL.md").exists():
            err(f"projection.omni.yaml: source {s} is not a skill")
    for d in skills:
        if f"skills/{d.name}" not in sources:
            err(f"{d.name}: not listed in projection.omni.yaml")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--guidelines", required=True)
    ap.add_argument("--schema")
    a = ap.parse_args()
    guidelines = Path(a.guidelines)
    if not (guidelines / "README.md").exists():
        sys.exit(f"not a guidelines folder: {guidelines}")
    skills = sorted(p for p in (ROOT / "skills").iterdir() if p.is_dir())
    if not skills:
        err("no skills found")
    for d in skills:
        check_skill(d, guidelines)
    check_manifest(skills, a.schema)
    print("\n".join(errors) or f"ok: {len(skills)} skills")
    sys.exit(1 if errors else 0)


main()
