from datetime import date
from typing import Any, List

from arxivmlrev import config

import pandas as pd
import pyperclip


def _readable_list(seq: List[Any]) -> str:
    # Ref: https://stackoverflow.com/a/53981846/
    seq = [str(s) for s in seq]
    if len(seq) < 3:
        return ' and '.join(seq)
    return ', '.join(seq[:-1]) + ', and ' + seq[-1]


def _linked_category(cat: str) -> str:
    return f'[{cat}](https://arxiv.org/list/{cat}/recent)'


categories = _readable_list(_linked_category(cat) for cat in sorted(config.CATEGORIES))

prologue = f"""
This is a mostly auto-generated list of review articles on machine learning and artificial intelligence that are on \
[arXiv](https://arxiv.org/). \
Although some of them were written for a specific technical audience or application, the techniques described are \
nonetheless generally relevant. \
The list is sorted reverse chronologically. It was generated on {date.today()}. \
It includes articles mainly from the arXiv categories {categories}.
"""

df = pd.read_csv(config.DATA_ARTICLES_CSV_PATH, dtype={'URL_ID': str, 'Category': 'category'})
with config.DATA_ARTICLES_MD_PATH.open('w') as md:
    md.write(f'# Review articles\n{prologue}\n')
    for _, row in df.iterrows():
        cat = _linked_category(row.Category)
        years = row.Year_Published if (row.Year_Published == row.Year_Updated) else \
            f'{row.Year_Published}-{row.Year_Updated}'
        link = f'https://arxiv.org/abs/{row.URL_ID}'
        md.write(f'* [{row.Title} ({years})]({link}) ({cat})\n')

pyperclip.copy(config.DATA_ARTICLES_MD_PATH.read_text())
# Note: pyperclip requires xclip or xsel, etc.
# Refer to https://pyperclip.readthedocs.io/en/latest/introduction.html#not-implemented-error
