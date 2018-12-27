from pathlib import Path

import data

import pandas as pd

DATA_DIR = Path(data.__path__._path[0])

CATEGORIES = {
    'cs.AI',
    'cs.CL',
    'cs.IR',
    'cs.LG',
    'cs.NE',
    # 'cs.CV',
    'stat.ML',
}

DELAY_BETWEEN_QUERIES = 4  # Per recommendation of 3 at https://arxiv.org/help/api/user-manual#paging
MAX_RESULTS_PER_QUERY = 400

TERMS = {  # Lowercase phrases only. Punctuation characters not allowed.
    'critical appraisal',
    'critical reflection',
    'brief history',
    'discussion',
    'foundations',
    'fundamentals',
    'introduction',
    'guide',
    'guidelines',
    'history of',
    'mathematics of',
    'perspectives',
    'overview',
    'recent advances',
    'review',
    'survey',
    'taxonomy',
    'tour',
    'tutorial',
}

TERMS_BLACKLIST = {  # Lowercase phrases only. Punctuation characters not allowed.
    'airline review',
    'app reviews',
    'arabic',
    'as a guide to',
    'assisted review',
    'automated driving',
    'autonomous driving',
    'blooms taxonomy',
    'book review',
    'cancer',
    'case study',
    'company fundamentals',
    'chinese',
    'competition',
    'conference',
    'conll',
    'discussion forum',
    'discussion threads',
    'eirex',
    'empirical',
    'europe',
    'generate review',
    'harvard business review',
    'heart',
    'hindi',
    'ibm',
    'in a taxonomy',
    'indian',
    'introduction of',
    'learning taxonomy',
    'matlab toolbox',
    'medical guidelines',
    'movie review',
    'myocardial',
    'norwegian',
    'online reviews',
    'patent',
    'pediatrics',
    'peer review',
    'peerus review',
    'product review',
    'punjabi',
    'review based',
    'review datasets',
    'review detection',
    'review helpfulness',
    'review rating',
    'review representations',
    'review selection',
    'review scores',
    'review spammers',
    'r package',
    'sinographic',
    'sports',
    'survey data',
    'survey evaluation',
    'survey extraction',
    'survey problem',
    'survey propagation',
    'survey questions',
    'taxonomy extraction',
    'taxonomy generation',
    'taxonomy induction',
    'taxonomy modification',
    'to guide',
    'tour problem',
    'tour recommendation',
    'tutorial generation',
    'twitter',
    'user review',
    'wikiconv',
    'wikipedia',
    'wsdm cup',
}

URL_ID_BLACKLIST = set(pd.read_csv(DATA_DIR / 'blacklist.csv', dtype={'URL_ID': str}, usecols=['URL_ID'])['URL_ID'])
