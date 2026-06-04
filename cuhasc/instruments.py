import csv
from pathlib import Path

INSTRUMENTS_DIR = Path(__file__).resolve().parent.parent / 'instruments'
SCALES_PATH = INSTRUMENTS_DIR / 'scales.csv'


def load_scales(path=None):
    if path is None:
        path = SCALES_PATH
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
            while len(labels) < levels:
                labels.append('')
            scales[name] = labels
    return scales


def load_questionnaire(path):
    items = []
    with open(path) as f:
        reader = csv.reader(f, delimiter='\t')
        next(reader)  # skip header
        for row in reader:
            if len(row) >= 2 and row[0].strip():
                items.append({
                    'item': row[0].strip(),
                    'scale': row[1].strip(),
                    'content': row[2].strip() if len(row) > 2 else '',
                })
    return items
