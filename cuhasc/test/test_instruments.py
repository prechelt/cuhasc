import pytest

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


def test_get_languages_requires_questionnaire_scales_and_dimensions(monkeypatch):
    # 'fr' has questionnaire + scales but no dimensions file -> excluded;
    # 'it' has questionnaire + dimensions but no scales -> excluded.
    monkeypatch.setattr(instruments, '_questionnaires', {'en': [], 'de': [], 'fr': [], 'it': []})
    monkeypatch.setattr(instruments, '_scales', {'en': {}, 'de': {}, 'fr': {}})
    monkeypatch.setattr(instruments, '_dimensions', {'en': {}, 'de': {}, 'it': {}})
    assert instruments.get_languages() == ['de', 'en']
