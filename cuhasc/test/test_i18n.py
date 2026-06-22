import cuhasc.i18n as i18n


def test_language_options_maps_codes_to_display_rows():
    options = i18n.language_options(['en', 'de'])
    assert options == [
        {'code': 'en', 'english': 'English', 'autonym': 'English', 'dir': 'ltr'},
        {'code': 'de', 'english': 'German', 'autonym': 'Deutsch', 'dir': 'ltr'},
    ]


def test_language_options_marks_rtl_languages():
    [option] = i18n.language_options(['ar'])
    assert option['dir'] == 'rtl'
    assert option['english'] == 'Arabic'
    assert option['autonym'] == 'العربية'


def test_language_options_falls_back_for_unknown_code():
    [option] = i18n.language_options(['xx'])
    assert option == {'code': 'xx', 'english': 'xx', 'autonym': 'xx', 'dir': 'ltr'}
