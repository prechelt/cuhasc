import pathlib

import pytest

import cuhasc
import cuhasc.instruments as instruments


def test_get_dimension_name_ok():
    assert instruments.get_dimension_name('PO', 'en') == 'Power Distance'
    assert instruments.get_dimension_name('PO', 'de') == 'Machtdistanz / Power Distance'


@pytest.mark.parametrize('language', ['en', 'de'])
def test_get_dimension_name_has_all_five_dimensions(language):
    assert instruments.DIMENSIONS == ('PO', 'UN', 'CO', 'LT', 'MA')
    for code in instruments.DIMENSIONS:
        name = instruments.get_dimension_name(code, language)
        assert isinstance(name, str) and name, f"missing {language} name for {code}"
    assert set(instruments._dimensions[language]) == set(instruments.DIMENSIONS), \
        f"{language} dimensions file and DIMENSIONS disagree"


def test_instruments_dir_lives_inside_the_package():
    # Guards the packaging: an INSTRUMENTS_DIR outside the package makes an installed wheel
    # find no questionnaires at all -- and silently, because glob() returns [] for a
    # non-existent directory, so the failure only surfaces as KeyError on the first request.
    assert instruments.INSTRUMENTS_DIR.is_relative_to(pathlib.Path(cuhasc.__file__).parent)
    assert len(instruments.get_languages()) >= 40
    assert 'en' in instruments.get_languages()


def test_get_questionnaire_ok():
    items = instruments.get_questionnaire('en')
    assert [item.item for item in items[:2]] == ['PO1', 'PO2']  # CSV order, unshuffled


def test_get_questionnaire_with_order_seed_has_expected_behavior():
    original = [item.item for item in instruments.get_questionnaire('en')]
    shuffled_a = [item.item for item in instruments.get_questionnaire('en', 'seed-a')]
    shuffled_a_again = [item.item for item in instruments.get_questionnaire('en', 'seed-a')]
    shuffled_b = [item.item for item in instruments.get_questionnaire('en', 'seed-b')]

    assert sorted(shuffled_a) == sorted(original)          # same items, no gain/loss
    assert shuffled_a != original                          # actually reordered
    assert shuffled_a == shuffled_a_again                  # same seed -> same order
    assert shuffled_a != shuffled_b                        # different seed -> different order
    assert [item.item for item in instruments.get_questionnaire('en')] == original  # global untouched


def test_get_languages_requires_questionnaire_scales_and_dimensions(monkeypatch):
    # 'fr' has questionnaire + scales but no dimensions file -> excluded;
    # 'it' has questionnaire + dimensions but no scales -> excluded.
    monkeypatch.setattr(instruments, '_questionnaires', {'en': [], 'de': [], 'fr': [], 'it': []})
    monkeypatch.setattr(instruments, '_scales', {'en': {}, 'de': {}, 'fr': {}})
    monkeypatch.setattr(instruments, '_dimensions', {'en': {}, 'de': {}, 'it': {}})
    assert instruments.get_languages() == ['de', 'en']
