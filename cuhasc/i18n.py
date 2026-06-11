"""
This data was compiled by Sonnet 4.6 2026-06-11 based on the following prompt:
"I need a JSON dictionary that maps each of the 2-letter ISO 639-1 language codes to 
a length-4 array of [full language name in English, full language name in the language's own script, 
RTL/LTR flag, low/mid/high resource indicator]. Build this for me. How reliable is it?"

The reliability assessment was this:

Field 1 — English name: ~99% reliable. These are the official ISO 639-1 English names, stable and well-documented.

Field 2 — Autonym (native script): ~90% reliable. The well-known languages are solid. 
For minor languages (Avestan, Church Slavic, Pali, some Pacific/African languages) there are often variant spellings 
or no universally agreed autonym. A few genuinely obscure ones (ae, cu, pi) have almost no 
living native community to validate against.

Field 3 — RTL/LTR: ~95% reliable, with known edge cases:
ha (Hausa): uses both Latin (Boko, modern standard) and Arabic (Ajami). 
Marked LTR for the dominant digital use, but RTL is equally valid for traditional contexts.
ku (Kurdish): Kurmanji dialect uses Latin (LTR); Sorani uses Arabic script (RTL). 
The single ku code is genuinely ambiguous — marked RTL as a conservative choice. 
BCP 47 kmr / ckb would distinguish them.
ks (Kashmiri): Nastaliq in Pakistan (RTL), Devanagari in India (LTR). 
Marked RTL as the more common encoding default.
pa (Punjabi): Gurmukhi in India (LTR), but Shahmukhi in Pakistan uses Arabic script (RTL). Marked LTR for Gurmukhi.

Field 4 — Resource level: ~85% reliable. This is the most subjective field. 
There's no official classification — it's a judgment call based on training corpus size, 
NLP benchmark coverage, and web presence. The high/mid/low boundaries are fuzzy; 
a researcher might reasonably argue about 20–30 entries in the mid/low borderland (e.g., sw, ne, my, be, eo). 
The high-resource group (27 languages) is the most defensible tier.
"""
language_map = {
  "aa": [
    "Afar",
    "Afaraf",
    "LTR",
    "low"
  ],
  "ab": [
    "Abkhazian",
    "Аҧсуа бызшәа",
    "LTR",
    "low"
  ],
  "ae": [
    "Avestan",
    "avesta",
    "LTR",
    "low"
  ],
  "af": [
    "Afrikaans",
    "Afrikaans",
    "LTR",
    "mid"
  ],
  "ak": [
    "Akan",
    "Akan",
    "LTR",
    "low"
  ],
  "am": [
    "Amharic",
    "አማርኛ",
    "LTR",
    "low"
  ],
  "an": [
    "Aragonese",
    "aragonés",
    "LTR",
    "low"
  ],
  "ar": [
    "Arabic",
    "العربية",
    "RTL",
    "high"
  ],
  "as": [
    "Assamese",
    "অসমীয়া",
    "LTR",
    "low"
  ],
  "av": [
    "Avaric",
    "авар мацӀ",
    "LTR",
    "low"
  ],
  "ay": [
    "Aymara",
    "aymar aru",
    "LTR",
    "low"
  ],
  "az": [
    "Azerbaijani",
    "azərbaycan dili",
    "LTR",
    "mid"
  ],
  "ba": [
    "Bashkir",
    "башҡорт теле",
    "LTR",
    "low"
  ],
  "be": [
    "Belarusian",
    "беларуская мова",
    "LTR",
    "mid"
  ],
  "bg": [
    "Bulgarian",
    "български език",
    "LTR",
    "mid"
  ],
  "bh": [
    "Bihari languages",
    "भोजपुरी",
    "LTR",
    "low"
  ],
  "bi": [
    "Bislama",
    "Bislama",
    "LTR",
    "low"
  ],
  "bm": [
    "Bambara",
    "bamanankan",
    "LTR",
    "low"
  ],
  "bn": [
    "Bengali",
    "বাংলা",
    "LTR",
    "mid"
  ],
  "bo": [
    "Tibetan",
    "བོད་ཡིག",
    "LTR",
    "low"
  ],
  "br": [
    "Breton",
    "brezhoneg",
    "LTR",
    "low"
  ],
  "bs": [
    "Bosnian",
    "bosanski jezik",
    "LTR",
    "mid"
  ],
  "ca": [
    "Catalan",
    "català",
    "LTR",
    "mid"
  ],
  "ce": [
    "Chechen",
    "нохчийн мотт",
    "LTR",
    "low"
  ],
  "ch": [
    "Chamorro",
    "Chamoru",
    "LTR",
    "low"
  ],
  "co": [
    "Corsican",
    "corsu",
    "LTR",
    "low"
  ],
  "cr": [
    "Cree",
    "ᓀᐦᐃᔭᐍᐏᐣ",
    "LTR",
    "low"
  ],
  "cs": [
    "Czech",
    "čeština",
    "LTR",
    "high"
  ],
  "cu": [
    "Church Slavic",
    "ѩзыкъ словѣньскъ",
    "LTR",
    "low"
  ],
  "cv": [
    "Chuvash",
    "чӑваш чӗлхи",
    "LTR",
    "low"
  ],
  "cy": [
    "Welsh",
    "Cymraeg",
    "LTR",
    "mid"
  ],
  "da": [
    "Danish",
    "dansk",
    "LTR",
    "high"
  ],
  "de": [
    "German",
    "Deutsch",
    "LTR",
    "high"
  ],
  "dv": [
    "Divehi",
    "ދިވެހި",
    "RTL",
    "low"
  ],
  "dz": [
    "Dzongkha",
    "རྫོང་ཁ",
    "LTR",
    "low"
  ],
  "ee": [
    "Ewe",
    "Eʋegbe",
    "LTR",
    "low"
  ],
  "el": [
    "Greek",
    "ελληνικά",
    "LTR",
    "high"
  ],
  "en": [
    "English",
    "English",
    "LTR",
    "high"
  ],
  "eo": [
    "Esperanto",
    "Esperanto",
    "LTR",
    "mid"
  ],
  "es": [
    "Spanish",
    "español",
    "LTR",
    "high"
  ],
  "et": [
    "Estonian",
    "eesti keel",
    "LTR",
    "mid"
  ],
  "eu": [
    "Basque",
    "euskara",
    "LTR",
    "mid"
  ],
  "fa": [
    "Persian",
    "فارسی",
    "RTL",
    "mid"
  ],
  "ff": [
    "Fula",
    "Fulfulde",
    "LTR",
    "low"
  ],
  "fi": [
    "Finnish",
    "suomi",
    "LTR",
    "high"
  ],
  "fj": [
    "Fijian",
    "vosa Vakaviti",
    "LTR",
    "low"
  ],
  "fo": [
    "Faroese",
    "føroyskt",
    "LTR",
    "low"
  ],
  "fr": [
    "French",
    "français",
    "LTR",
    "high"
  ],
  "fy": [
    "Western Frisian",
    "Frysk",
    "LTR",
    "low"
  ],
  "ga": [
    "Irish",
    "Gaeilge",
    "LTR",
    "mid"
  ],
  "gd": [
    "Scottish Gaelic",
    "Gàidhlig",
    "LTR",
    "low"
  ],
  "gl": [
    "Galician",
    "galego",
    "LTR",
    "mid"
  ],
  "gn": [
    "Guaraní",
    "Avañe'ẽ",
    "LTR",
    "low"
  ],
  "gu": [
    "Gujarati",
    "ગુજરાતી",
    "LTR",
    "mid"
  ],
  "gv": [
    "Manx",
    "Gaelg",
    "LTR",
    "low"
  ],
  "ha": [
    "Hausa",
    "Hausa",
    "LTR",
    "low"
  ],
  "he": [
    "Hebrew",
    "עברית",
    "RTL",
    "high"
  ],
  "hi": [
    "Hindi",
    "हिन्दी",
    "LTR",
    "high"
  ],
  "ho": [
    "Hiri Motu",
    "Hiri Motu",
    "LTR",
    "low"
  ],
  "hr": [
    "Croatian",
    "hrvatski jezik",
    "LTR",
    "mid"
  ],
  "ht": [
    "Haitian Creole",
    "Kreyòl ayisyen",
    "LTR",
    "low"
  ],
  "hu": [
    "Hungarian",
    "magyar",
    "LTR",
    "high"
  ],
  "hy": [
    "Armenian",
    "Հայերեն",
    "LTR",
    "mid"
  ],
  "hz": [
    "Herero",
    "Otjiherero",
    "LTR",
    "low"
  ],
  "ia": [
    "Interlingua",
    "Interlingua",
    "LTR",
    "low"
  ],
  "id": [
    "Indonesian",
    "Bahasa Indonesia",
    "LTR",
    "high"
  ],
  "ie": [
    "Interlingue",
    "Interlingue",
    "LTR",
    "low"
  ],
  "ig": [
    "Igbo",
    "Asụsụ Igbo",
    "LTR",
    "low"
  ],
  "ii": [
    "Sichuan Yi",
    "ꆈꌠ꒿ Nuosuhxop",
    "LTR",
    "low"
  ],
  "ik": [
    "Inupiaq",
    "Iñupiaq",
    "LTR",
    "low"
  ],
  "io": [
    "Ido",
    "Ido",
    "LTR",
    "low"
  ],
  "is": [
    "Icelandic",
    "Íslenska",
    "LTR",
    "mid"
  ],
  "it": [
    "Italian",
    "italiano",
    "LTR",
    "high"
  ],
  "iu": [
    "Inuktitut",
    "ᐃᓄᒃᑎᑐᑦ",
    "LTR",
    "low"
  ],
  "ja": [
    "Japanese",
    "日本語",
    "LTR",
    "high"
  ],
  "jv": [
    "Javanese",
    "basa Jawa",
    "LTR",
    "low"
  ],
  "ka": [
    "Georgian",
    "ქართული",
    "LTR",
    "mid"
  ],
  "kg": [
    "Kongo",
    "Kikongo",
    "LTR",
    "low"
  ],
  "ki": [
    "Kikuyu",
    "Gĩkũyũ",
    "LTR",
    "low"
  ],
  "kj": [
    "Kwanyama",
    "Kuanyama",
    "LTR",
    "low"
  ],
  "kk": [
    "Kazakh",
    "қазақ тілі",
    "LTR",
    "mid"
  ],
  "kl": [
    "Kalaallisut",
    "kalaallisut",
    "LTR",
    "low"
  ],
  "km": [
    "Khmer",
    "ខ្មែរ",
    "LTR",
    "low"
  ],
  "kn": [
    "Kannada",
    "ಕನ್ನಡ",
    "LTR",
    "mid"
  ],
  "ko": [
    "Korean",
    "한국어",
    "LTR",
    "high"
  ],
  "kr": [
    "Kanuri",
    "Kanuri",
    "LTR",
    "low"
  ],
  "ks": [
    "Kashmiri",
    "كٲشُر",
    "RTL",
    "low"
  ],
  "ku": [
    "Kurdish",
    "Kurdî / کوردی",
    "RTL",
    "low"
  ],
  "kv": [
    "Komi",
    "коми кыв",
    "LTR",
    "low"
  ],
  "kw": [
    "Cornish",
    "Kernewek",
    "LTR",
    "low"
  ],
  "ky": [
    "Kyrgyz",
    "Кыргызча",
    "LTR",
    "low"
  ],
  "la": [
    "Latin",
    "latine",
    "LTR",
    "mid"
  ],
  "lb": [
    "Luxembourgish",
    "Lëtzebuergesch",
    "LTR",
    "low"
  ],
  "lg": [
    "Ganda",
    "Luganda",
    "LTR",
    "low"
  ],
  "li": [
    "Limburgish",
    "Limburgs",
    "LTR",
    "low"
  ],
  "ln": [
    "Lingala",
    "Lingála",
    "LTR",
    "low"
  ],
  "lo": [
    "Lao",
    "ພາສາລາວ",
    "LTR",
    "low"
  ],
  "lt": [
    "Lithuanian",
    "lietuvių kalba",
    "LTR",
    "mid"
  ],
  "lu": [
    "Luba-Katanga",
    "Tshiluba",
    "LTR",
    "low"
  ],
  "lv": [
    "Latvian",
    "latviešu valoda",
    "LTR",
    "mid"
  ],
  "mg": [
    "Malagasy",
    "fiteny malagasy",
    "LTR",
    "low"
  ],
  "mh": [
    "Marshallese",
    "Kajin M̧ajeļ",
    "LTR",
    "low"
  ],
  "mi": [
    "Māori",
    "te reo Māori",
    "LTR",
    "low"
  ],
  "mk": [
    "Macedonian",
    "македонски јазик",
    "LTR",
    "mid"
  ],
  "ml": [
    "Malayalam",
    "മലയാളം",
    "LTR",
    "mid"
  ],
  "mn": [
    "Mongolian",
    "Монгол хэл",
    "LTR",
    "mid"
  ],
  "mr": [
    "Marathi",
    "मराठी",
    "LTR",
    "mid"
  ],
  "ms": [
    "Malay",
    "Bahasa Melayu",
    "LTR",
    "high"
  ],
  "mt": [
    "Maltese",
    "Malti",
    "LTR",
    "mid"
  ],
  "my": [
    "Burmese",
    "ဗမာစာ",
    "LTR",
    "low"
  ],
  "na": [
    "Nauru",
    "Dorerin Naoero",
    "LTR",
    "low"
  ],
  "nb": [
    "Norwegian Bokmål",
    "Norsk bokmål",
    "LTR",
    "high"
  ],
  "nd": [
    "Northern Ndebele",
    "isiNdebele",
    "LTR",
    "low"
  ],
  "ne": [
    "Nepali",
    "नेपाली",
    "LTR",
    "low"
  ],
  "ng": [
    "Ndonga",
    "Owambo",
    "LTR",
    "low"
  ],
  "nl": [
    "Dutch",
    "Nederlands",
    "LTR",
    "high"
  ],
  "nn": [
    "Norwegian Nynorsk",
    "Norsk nynorsk",
    "LTR",
    "mid"
  ],
  "no": [
    "Norwegian",
    "Norsk",
    "LTR",
    "high"
  ],
  "nr": [
    "Southern Ndebele",
    "isiNdebele",
    "LTR",
    "low"
  ],
  "nv": [
    "Navajo",
    "Diné bizaad",
    "LTR",
    "low"
  ],
  "ny": [
    "Chichewa",
    "chiCheŵa",
    "LTR",
    "low"
  ],
  "oc": [
    "Occitan",
    "occitan",
    "LTR",
    "low"
  ],
  "oj": [
    "Ojibwe",
    "ᐊᓂᔑᓈᐯᒧᐎᓐ",
    "LTR",
    "low"
  ],
  "om": [
    "Oromo",
    "Afaan Oromoo",
    "LTR",
    "low"
  ],
  "or": [
    "Odia",
    "ଓଡ଼ିଆ",
    "LTR",
    "low"
  ],
  "os": [
    "Ossetic",
    "ирон æвзаг",
    "LTR",
    "low"
  ],
  "pa": [
    "Punjabi",
    "ਪੰਜਾਬੀ",
    "LTR",
    "mid"
  ],
  "pi": [
    "Pali",
    "पाऴि",
    "LTR",
    "low"
  ],
  "pl": [
    "Polish",
    "język polski",
    "LTR",
    "high"
  ],
  "ps": [
    "Pashto",
    "پښتو",
    "RTL",
    "low"
  ],
  "pt": [
    "Portuguese",
    "português",
    "LTR",
    "high"
  ],
  "qu": [
    "Quechua",
    "Runa Simi",
    "LTR",
    "low"
  ],
  "rm": [
    "Romansh",
    "rumantsch grischun",
    "LTR",
    "low"
  ],
  "rn": [
    "Kirundi",
    "Ikirundi",
    "LTR",
    "low"
  ],
  "ro": [
    "Romanian",
    "limba română",
    "LTR",
    "high"
  ],
  "ru": [
    "Russian",
    "русский язык",
    "LTR",
    "high"
  ],
  "rw": [
    "Kinyarwanda",
    "Ikinyarwanda",
    "LTR",
    "low"
  ],
  "sa": [
    "Sanskrit",
    "संस्कृतम्",
    "LTR",
    "low"
  ],
  "sc": [
    "Sardinian",
    "sardu",
    "LTR",
    "low"
  ],
  "sd": [
    "Sindhi",
    "سنڌي",
    "RTL",
    "low"
  ],
  "se": [
    "Northern Sami",
    "Davvisámegiella",
    "LTR",
    "low"
  ],
  "sg": [
    "Sango",
    "yângâ tî sängö",
    "LTR",
    "low"
  ],
  "si": [
    "Sinhala",
    "සිංහල",
    "LTR",
    "low"
  ],
  "sk": [
    "Slovak",
    "slovenčina",
    "LTR",
    "mid"
  ],
  "sl": [
    "Slovenian",
    "slovenski jezik",
    "LTR",
    "mid"
  ],
  "sm": [
    "Samoan",
    "gagana fa'a Samoa",
    "LTR",
    "low"
  ],
  "sn": [
    "Shona",
    "chiShona",
    "LTR",
    "low"
  ],
  "so": [
    "Somali",
    "Soomaaliga",
    "LTR",
    "low"
  ],
  "sq": [
    "Albanian",
    "gjuha shqipe",
    "LTR",
    "mid"
  ],
  "sr": [
    "Serbian",
    "српски језик",
    "LTR",
    "mid"
  ],
  "ss": [
    "Swati",
    "SiSwati",
    "LTR",
    "low"
  ],
  "st": [
    "Southern Sotho",
    "Sesotho",
    "LTR",
    "low"
  ],
  "su": [
    "Sundanese",
    "Basa Sunda",
    "LTR",
    "low"
  ],
  "sv": [
    "Swedish",
    "svenska",
    "LTR",
    "high"
  ],
  "sw": [
    "Swahili",
    "Kiswahili",
    "LTR",
    "mid"
  ],
  "ta": [
    "Tamil",
    "தமிழ்",
    "LTR",
    "mid"
  ],
  "te": [
    "Telugu",
    "తెలుగు",
    "LTR",
    "mid"
  ],
  "tg": [
    "Tajik",
    "тоҷикӣ",
    "LTR",
    "low"
  ],
  "th": [
    "Thai",
    "ไทย",
    "LTR",
    "mid"
  ],
  "ti": [
    "Tigrinya",
    "ትግርኛ",
    "LTR",
    "low"
  ],
  "tk": [
    "Turkmen",
    "Türkmençe",
    "LTR",
    "low"
  ],
  "tl": [
    "Filipino",
    "Wikang Filipino",
    "LTR",
    "mid"
  ],
  "tn": [
    "Tswana",
    "Setswana",
    "LTR",
    "low"
  ],
  "to": [
    "Tonga",
    "faka Tonga",
    "LTR",
    "low"
  ],
  "tr": [
    "Turkish",
    "Türkçe",
    "LTR",
    "high"
  ],
  "ts": [
    "Tsonga",
    "Xitsonga",
    "LTR",
    "low"
  ],
  "tt": [
    "Tatar",
    "татар теле",
    "LTR",
    "low"
  ],
  "tw": [
    "Twi",
    "Twi",
    "LTR",
    "low"
  ],
  "ty": [
    "Tahitian",
    "Reo Tahiti",
    "LTR",
    "low"
  ],
  "ug": [
    "Uyghur",
    "ئۇيغۇرچە",
    "RTL",
    "low"
  ],
  "uk": [
    "Ukrainian",
    "українська мова",
    "LTR",
    "mid"
  ],
  "ur": [
    "Urdu",
    "اردو",
    "RTL",
    "mid"
  ],
  "uz": [
    "Uzbek",
    "Oʻzbek tili",
    "LTR",
    "mid"
  ],
  "ve": [
    "Venda",
    "Tshivenḓa",
    "LTR",
    "low"
  ],
  "vi": [
    "Vietnamese",
    "Tiếng Việt",
    "LTR",
    "mid"
  ],
  "vo": [
    "Volapük",
    "Volapük",
    "LTR",
    "low"
  ],
  "wa": [
    "Walloon",
    "walon",
    "LTR",
    "low"
  ],
  "wo": [
    "Wolof",
    "Wollof",
    "LTR",
    "low"
  ],
  "xh": [
    "Xhosa",
    "isiXhosa",
    "LTR",
    "low"
  ],
  "yi": [
    "Yiddish",
    "ייִדיש",
    "RTL",
    "low"
  ],
  "yo": [
    "Yoruba",
    "Yorùbá",
    "LTR",
    "low"
  ],
  "za": [
    "Zhuang",
    "Saɯ cueŋƅ",
    "LTR",
    "low"
  ],
  "zh": [
    "Chinese",
    "中文",
    "LTR",
    "high"
  ],
  "zu": [
    "Zulu",
    "isiZulu",
    "LTR",
    "low"
  ]
}