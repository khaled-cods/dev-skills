#!/usr/bin/env python3
"""Check every skills/*/SKILL.md: frontmatter, name, description. No dependencies."""
import re, sys, pathlib

root = pathlib.Path(__file__).resolve().parent.parent / "skills"
bad = 0
dirs = sorted(p for p in root.iterdir() if p.is_dir())
if not dirs:
    print("no skills found"); sys.exit(1)
for d in dirs:
    f = d / "SKILL.md"
    errs = []
    if not f.exists():
        errs.append("missing SKILL.md")
    else:
        t = f.read_text(encoding="utf-8")
        m = re.match(r"---\n(.*?)\n---\n(.+)", t, re.S)
        if not m:
            errs.append("frontmatter (--- ... ---) missing")
        else:
            fm = dict(re.findall(r"^([a-z-]+):\s*(.+)$", m.group(1), re.M))
            name, desc = fm.get("name", ""), fm.get("description", "")
            if name != d.name: errs.append(f"name '{name}' must equal folder '{d.name}'")
            if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name) or len(name) > 64: errs.append("name must be kebab-case, max 64 chars")
            if not desc: errs.append("description missing")
            if len(desc) > 1024: errs.append(f"description too long ({len(desc)} > 1024)")
            if "<" in desc or ">" in desc: errs.append("description must not contain angle brackets")
            if len(m.group(2).strip()) < 400: errs.append("body too short to be useful")
    print(("FAIL " if errs else "ok   ") + d.name + ("  -> " + "; ".join(errs) if errs else ""))
    bad += bool(errs)
print(f"\n{len(dirs)-bad}/{len(dirs)} skills valid")
sys.exit(1 if bad else 0)
