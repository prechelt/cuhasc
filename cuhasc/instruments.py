import csv
import glob as glob_module
from dataclasses import dataclass
from pathlib import Path

INSTRUMENTS_DIR = Path(__file__).resolve().parent.parent / 'instruments'

DIMENSIONS: tuple[str, ...] = ('PO', 'UN', 'CO', 'LT', 'MA')  # the five Hofstede Dimensions

_scales: dict = {}        # language code -> {scale_name: [labels]}
_questionnaires: dict = {}  # language code -> [Item]
_dimensions: dict = {}    # language code -> {dimension_code: name}


@dataclass
class Item:
    item: str
    scale: str
    content: str


def load_scales(glob: str):
    global _scales
    _scales = {}
    for path in sorted(glob_module.glob(glob)):
        stem = Path(path).stem
        lang = stem.split('-', 1)[1] if '-' in stem else stem  # remove base part of name, if any
        scales = {}
        with open(path) as f:
            reader = csv.reader(f, delimiter=';')
            next(reader)  # skip header
            for row in reader:
                if not row or not row[0].strip():
                    continue
                name = row[0].strip()
                levels = int(row[1])
                labels = list(row[2:2 + levels])
                assert levels == len(labels), f"{path}: '{row}' should have {levels} levels, but has {len(levels)}"
                scales[name] = labels
        _scales[lang] = scales


def load_questionnaires(glob: str):
    global _questionnaires
    _questionnaires = {}
    for path in sorted(glob_module.glob(glob)):
        stem = Path(path).stem
        lang = stem.split('-', 1)[1] if '-' in stem else stem
        items = []
        with open(path) as f:
            reader = csv.reader(f, delimiter='\t')
            next(reader)  # skip header
            for row in reader:
                if len(row) >= 2 and row[0].strip():
                    items.append(Item(
                        item=row[0].strip(),
                        scale=row[1].strip(),
                        content=row[2].strip() if len(row) > 2 else '',
                    ))
        _questionnaires[lang] = items


def load_dimensions(glob: str):
    global _dimensions
    _dimensions = {}
    for path in sorted(glob_module.glob(glob)):
        stem = Path(path).stem
        lang = stem.split('-', 1)[1] if '-' in stem else stem
        dims = {}  # maps dimension ID to dimension fullname, e.g. PO -> Power Distance
        with open(path) as f:
            reader = csv.reader(f, delimiter=';')
            next(reader)  # skip header
            for row in reader:
                if len(row) >= 2 and row[0].strip():
                    dims[row[0].strip()] = row[1].strip()
        _dimensions[lang] = dims


def get_languages() -> list[str]:
    """Languages that are fully translatable: questionnaire + scales + dimensions all present."""
    return sorted(set(_scales.keys()) & set(_questionnaires.keys()) & set(_dimensions.keys()))


def get_questionnaire(language: str) -> list[Item]:
    return _questionnaires[language]


def get_scales(language: str) -> dict:
    return _scales[language]


def get_dimension_name(code: str, language: str) -> str:
    return _dimensions[language][code]


load_scales(str(INSTRUMENTS_DIR / 'scales-*.csv'))
load_questionnaires(str(INSTRUMENTS_DIR / 'cvscale-*.tsv'))
load_dimensions(str(INSTRUMENTS_DIR / 'dimensions-*.csv'))
