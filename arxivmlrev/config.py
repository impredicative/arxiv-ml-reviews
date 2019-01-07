import logging.config
import math
from pathlib import Path
from typing import Set

import pandas as pd


def _textfile_set(path: Path) -> Set[str]:
    return set(path.read_text().strip().split('\n'))


CONFIG_DIR = Path(__file__).parent / '_config'
DATA_DIR = Path(__file__).parents[1] / 'data'

CATEGORIES = _textfile_set(Path(CONFIG_DIR) / 'categories.txt')
CONFIG_ARTICLES_PATH = CONFIG_DIR / 'articles.csv'
CONFIG_ARTICLES = pd.read_csv(CONFIG_ARTICLES_PATH, dtype={'URL_ID': str})
CONFIG_TERMS_PATH = CONFIG_DIR / 'terms.csv'
CONFIG_TERMS = pd.read_csv(CONFIG_TERMS_PATH)
DATA_ARTICLES_CSV_COLUMNS = ['URL_ID', 'Category', 'Title', 'Year_Published', 'Year_Updated', 'Abstract']
DATA_ARTICLES_CSV_PATH = DATA_DIR / 'articles.csv'
DATA_ARTICLES_MD_PATH = DATA_DIR / 'articles.md'
GITHUB_ACCESS_TOKEN_PATH = Path('~/.config/github').expanduser()
GITHUB_MD_PUBLISH_PATH = 'Resources/ArticlesReview.md'
GITHUB_PUBLISH_REPO = 'freenode-machinelearning/freenode-machinelearning.github.io'
LOGGING_CONF_PATH = CONFIG_DIR / 'logging.conf'
MAX_RESULTS_PER_QUERY = 1998
MIN_INTERVAL_BETWEEN_QUERIES = max(3., math.log(MAX_RESULTS_PER_QUERY))
TERMS_BLACKLIST = set(CONFIG_TERMS[CONFIG_TERMS['Presence'] == 0]['Term'])
TERMS_WHITELIST = set(CONFIG_TERMS[CONFIG_TERMS['Presence'] == 1]['Term'])  # Lowercase phrases without punctuation.
URL_ID_BLACKLIST = set(CONFIG_ARTICLES[CONFIG_ARTICLES['Presence'] == 0]['URL_ID'])
URL_ID_WHITELIST = set(CONFIG_ARTICLES[CONFIG_ARTICLES['Presence'] == 1]['URL_ID'])
URL_ID_WHITELIST_INTERSECTION_IGNORED = ['1707.08561']

logging.config.fileConfig(LOGGING_CONF_PATH)
logging.getLogger(__name__).info('Logging is configured.')
