#!/usr/bin/env python3
"""
scripts/fix_md_links.py

Fix common MkDocs “unrecognized relative link” issues by rewriting Markdown links
to point to real .md files (or index.md for directories), and cleaning up
path oddities like `.md/#anchor` -> `.md#anchor`.

What it fixes well (based on your log):
- ../03_preparing-fms            -> 03_preparing-fms.md (if it exists)
- ../../a380x-briefing/flight-deck -> ../a380x-briefing/flight-deck/index.md (if it exists)
- ../../foo/bar/baz              -> ../../foo/bar/baz.md (if it exists)
- ../simbrief.md/#setup...       -> ../simbrief.md#setup...
- Optional: convert absolute site links like /aircraft/common/flypados3/ to a relative index.md path.

What it does NOT try to auto-fix:
- Missing anchors (#something not on page) — those need content/heading fixes.

Usage:
  # Dry run (recommended first)
  python scripts/fix_md_links.py docs --dry-run

  # Write changes in-place
  python scripts/fix_md_links.py docs --write

  # Also convert absolute site-root links (/foo/bar/) when the target exists in docs/
  python scripts/fix_md_links.py docs --write --convert-absolute
"""

from __future__ import annotations

import argparse
import os
import posixpath
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple
from urllib.parse import urlsplit, urlunsplit


FENCE_RE = re.compile(r"^\s*(```|~~~)")  # simple fenced code block toggle
INLINE_LINK_RE = re.compile(r"(?<!\!)\[[^\]]*?\]\((?P<inside>[^)\n]+)\)")
REF_DEF_RE = re.compile(r"^(?P<lead>\[[^\]]+\]:\s*)(?P<url><[^>]+>|[^\s]+)(?P<rest>.*)$")

EXTERNAL_SCHEMES = {
    "http",
    "https",
    "mailto",
    "tel",
    "ftp",
    "ftps",
    "file",
    "data",
    "javascript",
}


def _posix_relpath(target: Path, base: Path) -> str:
    rel = os.path.relpath(target, base)
    return rel.replace(os.sep, "/")


def _norm_slug(s: str) -> str:
    # Normalizes a slug-ish string for fuzzy matching: remove non-alnum and lower it.
    return re.sub(r"[^a-z0-9]+", "", s.lower())


@dataclass(frozen=True)
class DocsIndex:
    docs_root: Path
    md_files: List[Path]  # absolute paths
    rel_md_files: List[str]  # posix paths relative to docs_root
    # key: rel path WITHOUT ".md" (posix), value: absolute md file path
    stem_to_abs: Dict[str, Path]
    # key: directory path (posix) -> absolute index.md (for folder links)
    dir_to_index_abs: Dict[str, Path]
    # key: normalized basename slug -> list of absolute md file paths
    slug_to_abs: Dict[str, List[Path]]
    # key: basename (file stem) -> list of absolute md file paths
    basename_to_abs: Dict[str, List[Path]]


def build_index(docs_root: Path) -> DocsIndex:
    md_files = sorted([p for p in docs_root.rglob("*.md") if p.is_file()])
    rel_md_files = [p.relative_to(docs_root).as_posix() for p in md_files]

    stem_to_abs: Dict[str, Path] = {}
    dir_to_index_abs: Dict[str, Path] = {}
    slug_to_abs: Dict[str, List[Path]] = {}
    basename_to_abs: Dict[str, List[Path]] = {}

    for abs_path, rel in zip(md_files, rel_md_files):
        stem = rel[:-3] if rel.endswith(".md") else rel
        stem_to_abs[stem] = abs_path

        base = Path(stem).name
        basename_to_abs.setdefault(base, []).append(abs_path)

        slug = _norm_slug(base)
        if slug:
            slug_to_abs.setdefault(slug, []).append(abs_path)

        # If this is an index.md, allow folder links to resolve to it
        if abs_path.name == "index.md":
            folder = Path(rel).parent.as_posix()
            dir_to_index_abs[folder] = abs_path

    return DocsIndex(
        docs_root=docs_root,
        md_files=md_files,
        rel_md_files=rel_md_files,
        stem_to_abs=stem_to_abs,
        dir_to_index_abs=dir_to_index_abs,
        slug_to_abs=slug_to_abs,
        basename_to_abs=basename_to_abs,
    )


def is_external_url(url: str) -> bool:
    # Keep anchors-only (#foo), and any URL with a known external scheme.
    if url.startswith("#"):
        return True
    parts = urlsplit(url)
    if parts.scheme and parts.scheme.lower() in EXTERNAL_SCHEMES:
        return True
    return False


def clean_md_anchor_slash(path_part: str) -> str:
    # Fix common typo: "something.md/" before a fragment or end.
    if path_part.endswith(".md/"):
        return path_part[:-1]
    return path_part


def resolve_to_abs(
        url_path: str,
        *,
        current_file_abs: Path,
        index: DocsIndex,
        convert_absolute: bool,
) -> Optional[Path]:
    """
    Resolve a markdown link "path" (no fragment) to an absolute .md target if possible.
    Returns target absolute path or None if not resolvable.
    """

    # Remove surrounding <...> is handled earlier; url_path is raw.
    url_path = url_path.strip()

    if not url_path:
        return None

    # Absolute site-root links (/foo/bar/): only resolve if convert_absolute is enabled.
    if url_path.startswith("/"):
        if not convert_absolute:
            return None
        rel = url_path.lstrip("/")
        rel = rel.strip()
        rel = rel.rstrip("/")
        if not rel:
            return None
        # Try folder -> index.md
        if rel in index.dir_to_index_abs:
            return index.dir_to_index_abs[rel]
        # Try exact .md
        abs_md = index.docs_root / f"{rel}.md"
        if abs_md.is_file():
            return abs_md
        # Try rel already includes .md
        abs_md2 = index.docs_root / rel
        if abs_md2.is_file() and abs_md2.suffix.lower() == ".md":
            return abs_md2
        # Try folder index
        abs_idx = index.docs_root / rel / "index.md"
        if abs_idx.is_file():
            return abs_idx
        return None

    # Relative links:
    # Compute normalized candidate relative-to-docs-root
    current_rel = current_file_abs.relative_to(index.docs_root).as_posix()
    current_dir = posixpath.dirname(current_rel)

    # Normalize (posix) to avoid OS-specific separators
    combined = posixpath.normpath(posixpath.join(current_dir, url_path))
    combined = combined.lstrip("./")

    # If it points to a folder that has index.md
    combined_no_trailing = combined.rstrip("/")
    if combined_no_trailing in index.dir_to_index_abs:
        return index.dir_to_index_abs[combined_no_trailing]

    # If it's already a .md file path
    if combined_no_trailing.endswith(".md"):
        abs_md = index.docs_root / combined_no_trailing
        if abs_md.is_file():
            return abs_md
        # Try without the ".md" lookup (in case of case/oddities)
        stem = combined_no_trailing[:-3]
        if stem in index.stem_to_abs:
            return index.stem_to_abs[stem]
    else:
        # Try "path.md"
        abs_md = index.docs_root / f"{combined_no_trailing}.md"
        if abs_md.is_file():
            return abs_md
        # Try "path/index.md"
        abs_idx = index.docs_root / combined_no_trailing / "index.md"
        if abs_idx.is_file():
            return abs_idx

    # Fuzzy fallback: search by basename / slug when link depth is wrong (e.g. ../../../airliner/...).
    # Avoid risky matches for empty/bad basenames.
    base = Path(combined_no_trailing).name
    if not base or base in {"index", "."}:
        return None

    # Prefer matches within the same top-level section (e.g., pilots-corner/)
    current_top = current_rel.split("/", 1)[0] if "/" in current_rel else current_rel
    candidates: List[Path] = []

    # 1) basename exact
    for p in index.basename_to_abs.get(base, []):
        candidates.append(p)

    # 2) slug match (handles hyphen differences like flight-deck vs flightdeck)
    slug = _norm_slug(base)
    for p in index.slug_to_abs.get(slug, []):
        if p not in candidates:
            candidates.append(p)

    if not candidates:
        return None

    # Score candidates: prefer same top-level folder; then prefer closer directory similarity
    def score(p: Path) -> Tuple[int, int]:
        relp = p.relative_to(index.docs_root).as_posix()
        top = relp.split("/", 1)[0] if "/" in relp else relp
        same_top = 0 if top == current_top else 1  # lower is better
        # directory similarity: count shared prefix segments
        cur_segs = current_dir.split("/") if current_dir else []
        tgt_segs = posixpath.dirname(relp).split("/") if posixpath.dirname(relp) else []
        shared = 0
        for a, b in zip(cur_segs, tgt_segs):
            if a == b:
                shared += 1
            else:
                break
        # higher shared is better => invert for sorting
        return (same_top, -shared)

    candidates_sorted = sorted(candidates, key=score)
    best = candidates_sorted[0]

    # If the best is ambiguous (multiple with same score), don't guess.
    best_score = score(best)
    tied = [p for p in candidates_sorted if score(p) == best_score]
    if len(tied) > 1:
        return None

    return best


def fix_url(
        url: str,
        *,
        current_file_abs: Path,
        index: DocsIndex,
        convert_absolute: bool,
) -> Optional[str]:
    """
    Returns a fixed URL (string) or None if no change.
    """
    if is_external_url(url):
        return None

    parts = urlsplit(url)
    if parts.scheme:  # unknown scheme, leave
        return None

    path_part = parts.path or ""
    frag = parts.fragment
    query = parts.query

    # Clean up path oddities
    path_part = clean_md_anchor_slash(path_part)

    # Another common typo: ".md/#anchor" ends up as path ".md/" and fragment "anchor"
    # We already remove trailing slash on ".md/" above.

    target_abs = resolve_to_abs(
        path_part,
        current_file_abs=current_file_abs,
        index=index,
        convert_absolute=convert_absolute,
    )
    if not target_abs:
        return None

    # Build new relative URL from current file directory
    new_rel = _posix_relpath(target_abs, current_file_abs.parent)

    # Preserve query/fragment
    new_parts = ("", "", new_rel, query, frag)
    new_url = urlunsplit(new_parts)

    if new_url == url:
        return None
    return new_url


def process_markdown_file(
        file_abs: Path,
        *,
        index: DocsIndex,
        convert_absolute: bool,
) -> Tuple[str, int]:
    """
    Returns (new_text, num_changes)
    """
    text = file_abs.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)

    in_fence = False
    fence_token = None

    total_changes = 0
    out_lines: List[str] = []

    def replace_inline(m: re.Match) -> str:
        nonlocal total_changes
        inside = m.group("inside")

        # split first URL token while preserving the remainder (titles etc.)
        mm = re.match(r"\s*(?P<url><[^>]+>|[^\s]+)(?P<rest>.*)", inside, flags=re.DOTALL)
        if not mm:
            return m.group(0)

        url_token = mm.group("url")
        rest = mm.group("rest") or ""

        wrapped = url_token.startswith("<") and url_token.endswith(">")
        url_raw = url_token[1:-1] if wrapped else url_token

        new_url = fix_url(
            url_raw,
            current_file_abs=file_abs,
            index=index,
            convert_absolute=convert_absolute,
        )
        if not new_url:
            return m.group(0)

        total_changes += 1
        new_token = f"<{new_url}>" if wrapped else new_url
        return m.group(0).replace(f"({inside})", f"({new_token}{rest})")

    def replace_ref_def(line: str) -> str:
        nonlocal total_changes
        m = REF_DEF_RE.match(line)
        if not m:
            return line
        lead = m.group("lead")
        url_token = m.group("url")
        rest = m.group("rest") or ""

        wrapped = url_token.startswith("<") and url_token.endswith(">")
        url_raw = url_token[1:-1] if wrapped else url_token

        new_url = fix_url(
            url_raw,
            current_file_abs=file_abs,
            index=index,
            convert_absolute=convert_absolute,
        )
        if not new_url:
            return line

        total_changes += 1
        new_token = f"<{new_url}>" if wrapped else new_url
        return f"{lead}{new_token}{rest}"

    for line in lines:
        fence_match = FENCE_RE.match(line)
        if fence_match:
            token = fence_match.group(1)
            if not in_fence:
                in_fence = True
                fence_token = token
            else:
                # close only if same token type
                if token == fence_token:
                    in_fence = False
                    fence_token = None
            out_lines.append(line)
            continue

        if in_fence:
            out_lines.append(line)
            continue

        # Apply reference definitions on their own lines
        line2 = replace_ref_def(line)

        # Apply inline link fixes
        line3 = INLINE_LINK_RE.sub(replace_inline, line2)

        out_lines.append(line3)

    return "".join(out_lines), total_changes


def iter_markdown_files(docs_root: Path) -> Iterable[Path]:
    for p in docs_root.rglob("*.md"):
        if p.is_file():
            yield p


def main() -> int:
    parser = argparse.ArgumentParser(description="Fix MkDocs markdown links to real .md / index.md targets.")
    parser.add_argument("docs_root", nargs="?", default="docs", help="Path to MkDocs docs_dir (default: docs)")
    parser.add_argument("--write", action="store_true", help="Write changes in-place (default: dry run)")
    parser.add_argument("--dry-run", action="store_true", help="Force dry-run (overrides --write)")
    parser.add_argument(
        "--convert-absolute",
        action="store_true",
        help="Also convert absolute site-root links like /foo/bar/ when the target exists under docs_root.",
    )

    args = parser.parse_args()

    docs_root = Path(args.docs_root).resolve()
    if not docs_root.is_dir():
        print(f"ERROR: docs_root not found or not a directory: {docs_root}", file=sys.stderr)
        return 2

    do_write = bool(args.write) and not bool(args.dry_run)

    index = build_index(docs_root)

    changed_files = 0
    total_changes = 0

    for file_abs in iter_markdown_files(docs_root):
        new_text, n = process_markdown_file(
            file_abs,
            index=index,
            convert_absolute=args.convert_absolute,
        )
        if n <= 0:
            continue

        changed_files += 1
        total_changes += n

        rel = file_abs.relative_to(docs_root).as_posix()
        print(f"{'WRITE' if do_write else 'DRY '}  {rel}  ({n} change{'s' if n != 1 else ''})")

        if do_write:
            file_abs.write_text(new_text, encoding="utf-8")

    print("")
    print(f"Done. Files changed: {changed_files}. Total link rewrites: {total_changes}.")
    if not do_write:
        print("Dry run only. Re-run with --write to apply changes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
