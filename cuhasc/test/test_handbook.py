import re

import pytest

import cuhasc.constants as c
import cuhasc.handbook as handbook
import cuhasc.instruments as instruments


def profile_of(*scores: dict) -> dict:
    """Team Culture Profile of one Member per given Culture Profile, plus the per-Dimension means."""
    members = [{'name': f"M{i}", 'profile': profile} for i, profile in enumerate(scores)]
    means = {}
    for dim in {dim for m in members for dim in m['profile']}:
        values = [m['profile'][dim] for m in members if dim in m['profile']]
        means[dim] = sum(values) / len(values)
    return {'members': members, 'means': means}


def test_evaluate_ok():
    lowish = profile_of({'PO': 1.0}, {'PO': 2.0})
    mixed = profile_of({'PO': 1.0}, {'PO': 4.0})
    highish = profile_of({'PO': 4.5}, {'PO': 5.0})
    # one-high / two-high: at least one resp. two Members at or above the high cutoff
    assert not handbook.evaluate('one-high(PO)', lowish)
    assert handbook.evaluate('one-high(PO)', mixed)
    assert handbook.evaluate('one-high(PO)', highish)
    assert not handbook.evaluate('two-high(PO)', lowish)
    assert not handbook.evaluate('two-high(PO)', mixed)  # only one Member is high
    assert handbook.evaluate('two-high(PO)', highish)
    # one-low / two-low: at least one resp. two Members at or below the low cutoff
    assert handbook.evaluate('one-low(PO)', lowish)
    assert handbook.evaluate('one-low(PO)', mixed)
    assert not handbook.evaluate('one-low(PO)', highish)
    assert handbook.evaluate('two-low(PO)', lowish)
    assert not handbook.evaluate('two-low(PO)', mixed)  # only one Member is low
    assert not handbook.evaluate('two-low(PO)', highish)
    # mean-high / mean-low: the team mean against the same cutoffs
    assert not handbook.evaluate('mean-high(PO)', lowish)   # mean 1.5
    assert handbook.evaluate('mean-low(PO)', lowish)
    assert not handbook.evaluate('mean-high(PO)', mixed)    # mean 2.5
    assert not handbook.evaluate('mean-low(PO)', mixed)
    assert handbook.evaluate('mean-high(PO)', highish)      # mean 4.75
    assert not handbook.evaluate('mean-low(PO)', highish)
    # every Dimension code is usable
    for dim in instruments.DIMENSIONS:
        assert handbook.evaluate(f"one-high({dim})", profile_of({dim: 5.0}))


def test_evaluate_at_the_cutoffs():
    """The cutoffs are inclusive on both sides."""
    assert handbook.evaluate('one-high(PO)', profile_of({'PO': c.HIGH_CUTOFF}))
    assert not handbook.evaluate('one-high(PO)', profile_of({'PO': c.HIGH_CUTOFF - 0.1}))
    assert handbook.evaluate('one-low(PO)', profile_of({'PO': c.LOW_CUTOFF}))
    assert not handbook.evaluate('one-low(PO)', profile_of({'PO': c.LOW_CUTOFF + 0.1}))
    assert handbook.evaluate('mean-high(PO)', profile_of({'PO': c.HIGH_CUTOFF}))
    assert handbook.evaluate('mean-low(PO)', profile_of({'PO': c.LOW_CUTOFF}))


def test_evaluate_ignores_members_lacking_the_dimension():
    """A Member without a Score for the Dimension neither satisfies nor blocks a Predicate."""
    assert handbook.evaluate('one-high(PO)', profile_of({'UN': 5.0}, {'PO': 5.0}))
    assert not handbook.evaluate('one-high(PO)', profile_of({'UN': 5.0}))
    assert handbook.evaluate('one-low(PO)', profile_of({'UN': 5.0}, {'PO': 1.0}))
    assert not handbook.evaluate('two-low(PO)', profile_of({'UN': 1.0}, {'PO': 1.0}))
    # a Dimension nobody answered has no mean to compare against
    assert not handbook.evaluate('mean-high(PO)', profile_of({'UN': 5.0}))
    assert not handbook.evaluate('mean-low(PO)', profile_of({'UN': 5.0}))


def test_evaluate_error():
    with pytest.raises(handbook.TriggerError, match='sometimes-high'):
        handbook.evaluate('sometimes-high(PO)', profile_of({'PO': 5.0}))
    with pytest.raises(handbook.TriggerError, match='all-low'):  # a Predicate that no longer exists
        handbook.evaluate('all-low(PO)', profile_of({'PO': 5.0}))
    with pytest.raises(handbook.TriggerError, match='XY'):
        handbook.evaluate('one-high(XY)', profile_of({'PO': 5.0}))
    for malformed in ['one-high', 'one-high(PO', 'one-high(PO))', 'one-high(PO) and two-low(UN)',
                      'one-high()', '', 'predicate_one_high(PO)', 'one-high(PO) ']:
        with pytest.raises(handbook.TriggerError, match='trigger'):
            handbook.evaluate(malformed, profile_of({'PO': 5.0}))


def test_registry_maps_the_six_fixed_predicate_names():
    assert sorted(handbook.PREDICATES) == ['mean-high', 'mean-low', 'one-high', 'one-low',
                                           'two-high', 'two-low']
    for name, predicate in handbook.PREDICATES.items():
        assert predicate(profile_of({'PO': 3.0}), 'PO') in (True, False), f"{name} must return a bool"


# ---- content loading ----

def write_section(tmp_path, filename: str, title: str = "A Title",
                   trigger: str = "one-high(PO)", body: str = "Some body text.\n"):
    path = tmp_path / filename
    path.write_text(f"---\ntitle: {title}\ntrigger: {trigger}\n---\n{body}")
    return path


def test_load_sections_reads_title_trigger_chapter_slug_body(tmp_path):
    write_section(tmp_path, "dailystandup-punctuality.md",
                  title="Punctuality", trigger="one-high(PO)", body="Show up on time.\n")
    handbook.load_sections(str(tmp_path / '*.md'))
    sections = handbook.get_sections_by_chapter()['dailystandup']
    assert len(sections) == 1
    section = sections[0]
    assert section.title == "Punctuality"
    assert section.trigger == "one-high(PO)"
    assert section.chapter == "dailystandup"
    assert section.slug == "dailystandup-punctuality"
    assert section.body == "Show up on time.\n"


def test_load_sections_derives_chapter_from_prefix_before_first_hyphen(tmp_path):
    write_section(tmp_path, "dailystandup-punctuality-issues.md")
    handbook.load_sections(str(tmp_path / '*.md'))
    section = handbook.get_sections_by_chapter()['dailystandup'][0]
    assert section.chapter == "dailystandup"
    assert section.slug == "dailystandup-punctuality-issues"


def test_get_sections_by_chapter_groups_and_orders_by_filename(tmp_path):
    write_section(tmp_path, "retro-b-second.md", title="Second")
    write_section(tmp_path, "dailystandup-a.md", title="DS-A")
    write_section(tmp_path, "retro-a-first.md", title="First")
    handbook.load_sections(str(tmp_path / '*.md'))
    by_chapter = handbook.get_sections_by_chapter()
    assert list(by_chapter.keys()) == ['dailystandup', 'retro']  # Chapters in filename order
    assert [s.title for s in by_chapter['retro']] == ['First', 'Second']  # filename order within Chapter


def test_missing_frontmatter_delimiters_aborts_naming_file(tmp_path):
    path = tmp_path / "dailystandup-broken.md"
    path.write_text("# just a plain Markdown file, no frontmatter\n")
    with pytest.raises(handbook.SectionError, match=re.escape(str(path))):
        handbook.load_sections(str(tmp_path / '*.md'))


def test_unparsable_yaml_aborts_naming_file(tmp_path):
    path = tmp_path / "dailystandup-broken.md"
    path.write_text("---\ntitle: [unclosed\ntrigger: one-high(PO)\n---\nBody.\n")
    with pytest.raises(handbook.SectionError, match=re.escape(str(path))):
        handbook.load_sections(str(tmp_path / '*.md'))


def test_missing_required_attribute_aborts_naming_file_and_attribute(tmp_path):
    path = tmp_path / "dailystandup-broken.md"
    path.write_text("---\ntitle: Missing Trigger\n---\nBody.\n")
    with pytest.raises(handbook.SectionError, match=f"{re.escape(str(path))}.*trigger"):
        handbook.load_sections(str(tmp_path / '*.md'))


def test_unknown_predicate_aborts_naming_file_and_predicate(tmp_path):
    path = write_section(tmp_path, "dailystandup-broken.md", trigger="sometimes-high(PO)")
    with pytest.raises(handbook.SectionError, match=f"{re.escape(str(path))}.*sometimes-high"):
        handbook.load_sections(str(tmp_path / '*.md'))


def test_unknown_dimension_aborts_naming_file_and_dimension(tmp_path):
    path = write_section(tmp_path, "dailystandup-broken.md", trigger="one-high(XY)")
    with pytest.raises(handbook.SectionError, match=f"{re.escape(str(path))}.*XY"):
        handbook.load_sections(str(tmp_path / '*.md'))


def test_malformed_trigger_grammar_aborts_naming_file(tmp_path):
    path = write_section(tmp_path, "dailystandup-broken.md", trigger="one-high(PO) and two-low(UN)")
    with pytest.raises(handbook.SectionError, match=f"{re.escape(str(path))}.*trigger"):
        handbook.load_sections(str(tmp_path / '*.md'))


# ---- image references (#10) ----

@pytest.fixture
def image_pool(tmp_path, monkeypatch):
    pool = tmp_path / 'img'
    pool.mkdir()
    monkeypatch.setattr(c, 'IMAGE_POOL_DIR', pool)
    return pool


def test_local_image_reference_rewritten_to_image_view_url(tmp_path, image_pool):
    (image_pool / 'foo.png').write_text('fake png bytes')
    write_section(tmp_path, "dailystandup-a.md", body="See ![alt text](foo.png) above.\n")
    handbook.load_sections(str(tmp_path / '*.md'))
    section = handbook.get_sections_by_chapter()['dailystandup'][0]
    assert section.body == "See ![alt text](/handbook/img/foo.png) above.\n"


def test_external_image_reference_with_scheme_left_unchanged(tmp_path, image_pool):
    write_section(tmp_path, "dailystandup-a.md", body="![alt](https://example.com/x.png)\n")
    handbook.load_sections(str(tmp_path / '*.md'))
    section = handbook.get_sections_by_chapter()['dailystandup'][0]
    assert section.body == "![alt](https://example.com/x.png)\n"


def test_external_image_reference_with_leading_slash_left_unchanged(tmp_path, image_pool):
    write_section(tmp_path, "dailystandup-a.md", body="![alt](/static/x.png)\n")
    handbook.load_sections(str(tmp_path / '*.md'))
    section = handbook.get_sections_by_chapter()['dailystandup'][0]
    assert section.body == "![alt](/static/x.png)\n"


def test_missing_local_image_aborts_naming_file_and_filename(tmp_path, image_pool):
    path = write_section(tmp_path, "dailystandup-broken.md", body="![alt](missing.png)\n")
    with pytest.raises(handbook.SectionError, match=f"{re.escape(str(path))}.*missing.png"):
        handbook.load_sections(str(tmp_path / '*.md'))


def test_external_image_reference_never_triggers_existence_check(tmp_path, image_pool):
    # no file created in image_pool at all; an external reference must not be checked
    write_section(tmp_path, "dailystandup-a.md", body="![alt](https://example.com/missing.png)\n")
    handbook.load_sections(str(tmp_path / '*.md'))  # must not raise
    section = handbook.get_sections_by_chapter()['dailystandup'][0]
    assert section.body == "![alt](https://example.com/missing.png)\n"


# ---- lookup by slug ----

def test_get_section_by_slug_returns_matching_section(tmp_path):
    write_section(tmp_path, "dailystandup-punctuality.md", title="Punctuality")
    handbook.load_sections(str(tmp_path / '*.md'))
    section = handbook.get_section_by_slug("dailystandup-punctuality")
    assert section is not None
    assert section.title == "Punctuality"


def test_get_section_by_slug_returns_none_for_unknown_slug(tmp_path):
    write_section(tmp_path, "dailystandup-punctuality.md")
    handbook.load_sections(str(tmp_path / '*.md'))
    assert handbook.get_section_by_slug("no-such-slug") is None
