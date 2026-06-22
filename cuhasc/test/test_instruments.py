import pytest

import cuhasc.instruments as instruments


def test_get_dimension_name_ok():
    assert instruments.get_dimension_name('PO', 'en') == 'Power Distance'
    assert instruments.get_dimension_name('PO', 'de') == 'Machtdistanz'


@pytest.mark.parametrize('language', ['en', 'de'])
def test_get_dimension_name_has_all_five_dimensions(language):
    for code in ['PO', 'UN', 'CO', 'LT', 'MA']:
        name = instruments.get_dimension_name(code, language)
        assert isinstance(name, str) and name, f"missing {language} name for {code}"
