# python
"""
scripts/fix_md_links.py
Scan Markdown files and append `.md` to relative links when the corresponding .md file exists.
Usage:
  python scripts/fix_md_links.py         # dry run (shows proposed changes)
  python scripts/fix_md_links.py --apply # apply changes (creates .bak backups)
"""

import argparse
import os
import re
from pathlib import Path

EXCLUDE_DIRS = {".git", "node_modules", "venv", ".venv", "__pycache__"}

LINK_RE = re.compile(r'(!?)\[(.*?)\]\(([^)]+)\)')

def is_external(target: str) -> bool:
    return target.startswith(("http://", "https://", "mailto:", "tel:")) or target.startswith("/")

# python
def find_md_candidate(base_dir: Path, target_path: str) -> str | None:
    # split fragment
    if "#" in target_path:
        path_part, frag = target_path.split("#", 1)
        frag = "#" + frag
    else:
        path_part, frag = target_path, ""
    if path_part == "" or path_part.endswith("/"):
        # directory - check index.md or README.md
        cand_dir = (base_dir / path_part).resolve()
        for idx in ("index.md", "README.md"):
            if (cand_dir / idx).exists():
                rel = os.path.relpath((cand_dir / idx).resolve(), base_dir).replace("\\", "/")
                return rel + frag
        return None
    # If path_part points to an existing directory (without trailing slash), accept index files too
    cand_dir_no_slash = (base_dir / path_part)
    if cand_dir_no_slash.exists() and cand_dir_no_slash.is_dir():
        for idx in ("index.md", "README.md"):
            if (cand_dir_no_slash / idx).exists():
                rel = os.path.relpath((cand_dir_no_slash / idx).resolve(), base_dir).replace("\\", "/")
                return rel + frag
    # If already has an extension, skip
    if Path(path_part).suffix:
        return None
    # candidate with .md relative to the md file's directory
    candidate = (base_dir / path_part).with_suffix(".md").resolve()
    if candidate.exists():
        rel = os.path.relpath(candidate, base_dir).replace("\\", "/")
        return rel + frag
    # also check relative path without normalizing base_dir (handles ../../)
    candidate2 = (base_dir / (path_part + ".md")).resolve()
    if candidate2.exists():
        rel = os.path.relpath(candidate2, base_dir).replace("\\", "/")
        return rel + frag
    return None

def process_file(path: Path, apply: bool) -> bool:
    text = path.read_text(encoding="utf-8")
    changed = False
    def repl(m):
        nonlocal changed
        bang, label, target = m.groups()
        if is_external(target) or target.startswith("#"):
            return m.group(0)
        # preserve leading spaces in target
        candidate = find_md_candidate(path.parent, target)
        if candidate:
            changed = True
            return f"{bang}[{label}]({candidate})"
        return m.group(0)
    new_text = LINK_RE.sub(repl, text)
    if changed:
        if apply:
            bak = path.with_suffix(path.suffix + ".bak")
            if not bak.exists():
                bak.write_bytes(text.encode("utf-8"))
            path.write_text(new_text, encoding="utf-8")
            print(f"UPDATED: {path}")
        else:
            print(f"DRY RUN - would update: {path}")
    return changed

def main():
    parser = argparse.ArgumentParser(description="Fix missing .md extensions in relative links")
    parser.add_argument("--apply", action="store_true", help="Apply changes (create .bak backups).")
    args = parser.parse_args()
    repo_root = Path(".").resolve()
    any_changes = False
    for root, dirs, files in os.walk(repo_root):
        # prune excluded dirs
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS and not d.startswith(".")]
        for f in files:
            if not f.endswith(".md"):
                continue
            p = Path(root) / f
            try:
                if process_file(p, args.apply):
                    any_changes = True
            except Exception as e:
                print(f"ERROR processing {p}: {e}")
    if not any_changes:
        print("No changes detected.")

if __name__ == "__main__":
    main()
