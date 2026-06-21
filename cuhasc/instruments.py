import csv
import glob as glob_module
from dataclasses import dataclass
from pathlib import Path

INSTRUMENTS_DIR = Path(__file__).resolve().parent.parent / 'instruments'

_scales: dict = {}        # language code -> {scale_name: [labels]}
_questionnaires: dict = {}  # language code -> [Item]


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
        lang = stem.split('-', 1)[1] if '-' in stem else stem
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
                assert levels == len(labels)
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


def get_languages() -> list[str]:
    return sorted(set(_scales.keys()) & set(_questionnaires.keys()))


def get_questionnaire(language: str) -> list[Item]:
    return _questionnaires[language]


def get_scales(language: str) -> dict:
    return _scales[language]


load_scales(str(INSTRUMENTS_DIR / 'scales-*.csv'))
load_questionnaires(str(INSTRUMENTS_DIR / 'cvscale-*.tsv'))
