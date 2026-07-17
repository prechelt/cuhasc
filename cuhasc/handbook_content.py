"""Content loading for the Handbook: parses Section files into memory at import time.

Mirrors the eager-load-at-import pattern of ``instruments.py``. Each Section file lives
in the handbook content directory, named ``chaptername-keywords.md``, holding YAML
frontmatter (``title``, ``trigger``) followed by a ``---`` line and a Markdown body.
"""

import glob as glob_module
import re
from dataclasses import dataclass
from pathlib import Path

import yaml

import cuhasc.handbook as handbook

HANDBOOK_DIR = Path(__file__).resolve().parent.parent / 'handbook'
IMAGE_POOL_DIR = HANDBOOK_DIR / 'img'
IMAGE_URL_PREFIX = '/handbook/img/'

REQUIRED_ATTRS = {"title", "trigger"}

FRONTMATTER_REGEXP = re.compile(r"^---\n(.*?\n)---\n(.*)$", re.DOTALL)
IMAGE_REF_REGEXP = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
_URL_SCHEME_REGEXP = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*://")

# a placeholder Team Culture Profile with no Members: safe to evaluate any valid
# trigger against, since it can only ever make a Predicate return False, never raise.
_EMPTY_PROFILE = {'members': [], 'means': {}}


class SectionError(ValueError):
    """An invalid Section file. Its message names the offending file and problem."""


@dataclass
class Section:
    title: str
    trigger: str
    chapter: str
    slug: str
    body: str


_sections: list[Section] = []


def load_sections(glob: str):
    global _sections
    _sections = []
    for path in sorted(glob_module.glob(glob)):
        _sections.append(_load_one(Path(path)))


def _load_one(path: Path) -> Section:
    frontmatter, body = _parse_frontmatter(path)
    trigger = frontmatter['trigger']
    try:
        handbook.evaluate(trigger, _EMPTY_PROFILE)
    except handbook.TriggerError as e:
        raise SectionError(f"{path}: {e}") from e
    body = _resolve_images(path, body)
    stem = path.stem
    chapter = stem.split('-', 1)[0]
    return Section(title=frontmatter['title'], trigger=trigger, chapter=chapter, slug=stem, body=body)


def _is_local_image_ref(target: str) -> bool:
    return not target.startswith('/') and not _URL_SCHEME_REGEXP.match(target)


def _resolve_images(path: Path, body: str) -> str:
    """Rewrite local image references to the handbook_image view's URL, verifying
    each referenced file exists in the image pool. External references (a scheme or
    a leading '/') are passed through unchanged and never checked for existence."""
    def replace(match: re.Match) -> str:
        alt, target = match.group(1), match.group(2)
        if not _is_local_image_ref(target):
            return match.group(0)
        if not (IMAGE_POOL_DIR / target).is_file():
            raise SectionError(f"{path}: missing local image file: {target}")
        return f"![{alt}]({IMAGE_URL_PREFIX}{target})"
    return IMAGE_REF_REGEXP.sub(replace, body)


def _parse_frontmatter(path: Path) -> tuple[dict, str]:
    text = path.read_text()
    match = FRONTMATTER_REGEXP.match(text)
    if not match:
        raise SectionError(f"{path}: missing YAML frontmatter delimited by '---' lines")
    yaml_text, body = match.groups()
    try:
        frontmatter = yaml.safe_load(yaml_text)
    except yaml.YAMLError as e:
        raise SectionError(f"{path}: unparsable YAML frontmatter: {e}") from e
    if not isinstance(frontmatter, dict):
        raise SectionError(f"{path}: frontmatter must be a YAML mapping with {sorted(REQUIRED_ATTRS)}")
    missing = REQUIRED_ATTRS - frontmatter.keys()
    if missing:
        raise SectionError(f"{path}: missing required frontmatter attribute(s): {', '.join(sorted(missing))}")
    return frontmatter, body


def get_section_by_slug(slug: str) -> Section | None:
    for section in _sections:
        if section.slug == slug:
            return section
    return None


def get_sections_by_chapter() -> dict[str, list[Section]]:
    """The loaded Sections grouped by Chapter, in filename order within each Chapter,
    and Chapters in filename order."""
    result: dict[str, list[Section]] = {}
    for section in _sections:
        result.setdefault(section.chapter, []).append(section)
    return result


load_sections(str(HANDBOOK_DIR / '*.md'))
