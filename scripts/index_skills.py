# -*- coding: utf-8 -*-
"""Scan every skill library on this machine and print/emit an index.

Usage:
    python index_skills.py                 # print the inventory
    python index_skills.py --out DIR       # also write index.md / index.csv / index.json into DIR

Reads only the frontmatter (name / description) of each SKILL.md, so it stays fast
even when a library carries a multi-GB runtime folder.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

DEFAULT_ROOTS = [
    r"F:\SKIILS仓库",
    r"F:\COdebuddy生产文件",
    r"F:\马维斯生产文件",
    r"F:\CROW5",
    r"C:\Users\Administrator\.agents\skills",
    r"C:\Users\Administrator\.workbuddy\skills",
]
SKIP_DIRS = {"node_modules", ".git", "__pycache__", "dist", "dist14", "dist15", "build", ".venv", "venv"}
NAME_RE = re.compile(r"^name:\s*(.+?)\s*$", re.M)
DESC_RE = re.compile(r"^description:\s*(.+?)\s*$", re.M)
H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.M)


def read_front(path: Path) -> tuple[str, str, str]:
    try:
        with path.open("r", encoding="utf-8", errors="replace") as f:
            head = f.read(6000)
    except OSError:
        return path.parent.name, "", ""
    name = NAME_RE.search(head)
    desc = DESC_RE.search(head)
    h1 = H1_RE.search(head)
    n = (name.group(1) if name else (h1.group(1) if h1 else path.parent.name)).strip().strip('"\'')
    d = (desc.group(1) if desc else "").strip().strip('"\'')
    return n, d, head


def scan(root: Path) -> list[dict]:
    rows: list[dict] = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        if "SKILL.md" not in filenames:
            continue
        p = Path(dirpath) / "SKILL.md"
        name, desc, _ = read_front(p)
        rel = str(p.relative_to(root)).replace("\\", "/")
        category = rel.split("/")[0] if "/" in rel else "(root)"
        rows.append({
            "技能名": name,
            "分类": category,
            "触发时机/说明": desc[:160],
            "来源库": str(root),
            "相对路径": rel,
            "字节": p.stat().st_size,
        })
    return rows


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=None, help="directory to write index.md / index.csv / index.json into")
    ap.add_argument("--root", action="append", default=None, help="extra/replacement root (repeatable)")
    args = ap.parse_args()

    roots = [Path(r) for r in (args.root or DEFAULT_ROOTS)]
    all_rows: list[dict] = []
    per_root: list[tuple[str, int]] = []
    for r in roots:
        if not r.is_dir():
            print(f"[skip] not found: {r}")
            continue
        rows = scan(r)
        per_root.append((str(r), len(rows)))
        all_rows.extend(rows)

    print("== skill libraries ==")
    for r, n in per_root:
        print(f"  {n:>4}  {r}")
    print(f"  total {len(all_rows)} skills\n")

    for r, _ in per_root:
        rows = [x for x in all_rows if x["来源库"] == r]
        if not rows:
            continue
        print(f"--- {r} ---")
        for x in sorted(rows, key=lambda x: x["相对路径"]):
            print(f"  {x['技能名']:<38} | {x['分类']:<14} | {x['触发时机/说明'][:70]}")
        print()

    if args.out:
        out = Path(args.out)
        out.mkdir(parents=True, exist_ok=True)
        (out / "skills.json").write_text(json.dumps(all_rows, ensure_ascii=False, indent=2), encoding="utf-8")
        with (out / "skills.csv").open("w", encoding="utf-8-sig", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(all_rows[0].keys()) if all_rows else ["技能名"])
            w.writeheader()
            w.writerows(all_rows)
        md = ["# Skill library index", "", f"- libraries scanned: {len(per_root)}",
              f"- skills found: {len(all_rows)}", ""]
        for r, _ in per_root:
            rows = [x for x in all_rows if x["来源库"] == r]
            if not rows:
                continue
            md += [f"## {r}  ({len(rows)})", "", "| skill | category | when to use | path |", "| --- | --- | --- | --- |"]
            for x in sorted(rows, key=lambda x: x["相对路径"]):
                md.append(f"| {x['技能名']} | {x['分类']} | {str(x['触发时机/说明'])[:90].replace('|', '/')} | {x['相对路径']} |")
            md.append("")
        (out / "skills-index.md").write_text("\n".join(md), encoding="utf-8")
        print(f"[written] {out}\\skills-index.md , skills.csv , skills.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
