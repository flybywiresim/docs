"""Render public upstream Markdown with the links needed by the docs."""

import re
from functools import lru_cache
from urllib.error import URLError
from urllib.parse import urljoin
from urllib.request import urlopen


HEADING = re.compile(r"^ {0,3}(#{1,6})[ \t]+")
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
INLINE_LINK = re.compile(r"(\]\(\s*<?)([^\s)>]+)")


def select_section(markdown, section, url):
    """Return the content below a heading through its last subsection."""
    lines = markdown.splitlines(keepends=True)
    start = None
    level = None
    fence = None
    for index, line in enumerate(lines):
        marker = FENCE.match(line)
        if fence:
            if marker and marker[1].startswith(fence) and not marker[2].strip():
                fence = None
            continue
        if marker:
            fence = marker[1]
            continue
        heading = HEADING.match(line)
        if heading is None:
            continue
        if start is None and line.strip().casefold() == section.casefold():
            start = index + 1
            level = len(heading[1])
        elif start is not None and len(heading[1]) <= level:
            return "".join(lines[start:index])
    if start is None:
        raise ValueError(f"Required heading {section!r} not found in {url}")
    return "".join(lines[start:])


def define_env(env):
    @lru_cache(maxsize=None)
    def fetch(url):
        try:
            with urlopen(url, timeout=20) as response:
                return response.read().decode("utf-8-sig"), response.geturl()
        except (URLError, TimeoutError, UnicodeError) as error:
            raise ValueError(f"Could not load required Markdown from {url}: {error}") from error

    @env.macro
    def external_markdown(url, section="", fragment_map=None):
        markdown, source_url = fetch(url)
        content = select_section(markdown, section, url) if section else markdown.partition("\n")[2]
        if not content.strip():
            raise ValueError(f"Required Markdown {section or 'content'!r} is empty in {url}")

        def rebase_link(match):
            target = match[2]
            if target.startswith("#"):
                target = (fragment_map or {}).get(target, target)
            else:
                target = urljoin(source_url, target)
            return match[1] + target

        return INLINE_LINK.sub(rebase_link, content)
