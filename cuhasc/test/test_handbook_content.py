import re

import pytest

import cuhasc.handbook_content as handbook_content


def write_section(tmp_path, filename: str, title: str = "A Title",
                   trigger: str = "one-high(PO)", body: str = "Some body text.\n"):
    path = tmp_path / filename
    path.write_text(f"---\ntitle: {title}\ntrigger: {trigger}\n---\n{body}")
    return path


def test_load_sections_reads_title_trigger_chapter_slug_body(tmp_path):
    write_section(tmp_path, "dailystandup-punctuality.md",
                  title="Punctuality", trigger="one-high(PO)", body="Show up on time.\n")
    handbook_content.load_sections(str(tmp_path / '*.md'))
    sections = handbook_content.get_sections_by_chapter()['dailystandup']
    assert len(sections) == 1
    section = sections[0]
    assert section.title == "Punctuality"
    assert section.trigger == "one-high(PO)"
    assert section.chapter == "dailystandup"
    assert section.slug == "dailystandup-punctuality"
    assert section.body == "Show up on time.\n"


def test_load_sections_derives_chapter_from_prefix_before_first_hyphen(tmp_path):
    write_section(tmp_path, "dailystandup-punctuality-issues.md")
    handbook_content.load_sections(str(tmp_path / '*.md'))
    section = handbook_content.get_sections_by_chapter()['dailystandup'][0]
    assert section.chapter == "dailystandup"
    assert section.slug == "dailystandup-punctuality-issues"


def test_get_sections_by_chapter_groups_and_orders_by_filename(tmp_path):
    write_section(tmp_path, "retro-b-second.md", title="Second")
    write_section(tmp_path, "dailystandup-a.md", title="DS-A")
    write_section(tmp_path, "retro-a-first.md", title="First")
    handbook_content.load_sections(str(tmp_path / '*.md'))
    by_chapter = handbook_content.get_sections_by_chapter()
    assert list(by_chapter.keys()) == ['dailystandup', 'retro']  # Chapters in filename order
    assert [s.title for s in by_chapter['retro']] == ['First', 'Second']  # filename order within Chapter


def test_missing_frontmatter_delimiters_aborts_naming_file(tmp_path):
    path = tmp_path / "dailystandup-broken.md"
    path.write_text("# just a plain Markdown file, no frontmatter\n")
    with pytest.raises(handbook_content.SectionError, match=re.escape(str(path))):
        handbook_content.load_sections(str(tmp_path / '*.md'))


def test_unparsable_yaml_aborts_naming_file(tmp_path):
    path = tmp_path / "dailystandup-broken.md"
    path.write_text("---\ntitle: [unclosed\ntrigger: one-high(PO)\n---\nBody.\n")
    with pytest.raises(handbook_content.SectionError, match=re.escape(str(path))):
        handbook_content.load_sections(str(tmp_path / '*.md'))


def test_missing_required_attribute_aborts_naming_file_and_attribute(tmp_path):
    path = tmp_path / "dailystandup-broken.md"
    path.write_text("---\ntitle: Missing Trigger\n---\nBody.\n")
    with pytest.raises(handbook_content.SectionError, match=f"{re.escape(str(path))}.*trigger"):
        handbook_content.load_sections(str(tmp_path / '*.md'))


def test_unknown_predicate_aborts_naming_file_and_predicate(tmp_path):
    path = write_section(tmp_path, "dailystandup-broken.md", trigger="sometimes-high(PO)")
    with pytest.raises(handbook_content.SectionError, match=f"{re.escape(str(path))}.*sometimes-high"):
        handbook_content.load_sections(str(tmp_path / '*.md'))


def test_unknown_dimension_aborts_naming_file_and_dimension(tmp_path):
    path = write_section(tmp_path, "dailystandup-broken.md", trigger="one-high(XY)")
    with pytest.raises(handbook_content.SectionError, match=f"{re.escape(str(path))}.*XY"):
        handbook_content.load_sections(str(tmp_path / '*.md'))


def test_malformed_trigger_grammar_aborts_naming_file(tmp_path):
    path = write_section(tmp_path, "dailystandup-broken.md", trigger="one-high(PO) and two-low(UN)")
    with pytest.raises(handbook_content.SectionError, match=f"{re.escape(str(path))}.*trigger"):
        handbook_content.load_sections(str(tmp_path / '*.md'))


# ---- image references (#10) ----

@pytest.fixture
def image_pool(tmp_path, monkeypatch):
    pool = tmp_path / 'img'
    pool.mkdir()
    monkeypatch.setattr(handbook_content, 'IMAGE_POOL_DIR', pool)
    return pool


def test_local_image_reference_rewritten_to_image_view_url(tmp_path, image_pool):
    (image_pool / 'foo.png').write_text('fake png bytes')
    write_section(tmp_path, "dailystandup-a.md", body="See ![alt text](foo.png) above.\n")
    handbook_content.load_sections(str(tmp_path / '*.md'))
    section = handbook_content.get_sections_by_chapter()['dailystandup'][0]
    assert section.body == "See ![alt text](/handbook/img/foo.png) above.\n"


def test_external_image_reference_with_scheme_left_unchanged(tmp_path, image_pool):
    write_section(tmp_path, "dailystandup-a.md", body="![alt](https://example.com/x.png)\n")
    handbook_content.load_sections(str(tmp_path / '*.md'))
    section = handbook_content.get_sections_by_chapter()['dailystandup'][0]
    assert section.body == "![alt](https://example.com/x.png)\n"


def test_external_image_reference_with_leading_slash_left_unchanged(tmp_path, image_pool):
    write_section(tmp_path, "dailystandup-a.md", body="![alt](/static/x.png)\n")
    handbook_content.load_sections(str(tmp_path / '*.md'))
    section = handbook_content.get_sections_by_chapter()['dailystandup'][0]
    assert section.body == "![alt](/static/x.png)\n"


def test_missing_local_image_aborts_naming_file_and_filename(tmp_path, image_pool):
    path = write_section(tmp_path, "dailystandup-broken.md", body="![alt](missing.png)\n")
    with pytest.raises(handbook_content.SectionError, match=f"{re.escape(str(path))}.*missing.png"):
        handbook_content.load_sections(str(tmp_path / '*.md'))


def test_external_image_reference_never_triggers_existence_check(tmp_path, image_pool):
    # no file created in image_pool at all; an external reference must not be checked
    write_section(tmp_path, "dailystandup-a.md", body="![alt](https://example.com/missing.png)\n")
    handbook_content.load_sections(str(tmp_path / '*.md'))  # must not raise
    section = handbook_content.get_sections_by_chapter()['dailystandup'][0]
    assert section.body == "![alt](https://example.com/missing.png)\n"


# ---- lookup by slug ----

def test_get_section_by_slug_returns_matching_section(tmp_path):
    write_section(tmp_path, "dailystandup-punctuality.md", title="Punctuality")
    handbook_content.load_sections(str(tmp_path / '*.md'))
    section = handbook_content.get_section_by_slug("dailystandup-punctuality")
    assert section is not None
    assert section.title == "Punctuality"


def test_get_section_by_slug_returns_none_for_unknown_slug(tmp_path):
    write_section(tmp_path, "dailystandup-punctuality.md")
    handbook_content.load_sections(str(tmp_path / '*.md'))
    assert handbook_content.get_section_by_slug("no-such-slug") is None
