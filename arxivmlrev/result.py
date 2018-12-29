from dataclasses import dataclass
from string import punctuation
from typing import Dict, Set, Union

from arxivmlrev import config


@dataclass
class Result:
    result: dict

    @property
    def _title_cmp(self) -> str:
        """Return the modified title used for comparison against a whitelist or blacklist."""
        return ''.join(c for c in self.title.lower() if c not in punctuation)

    @property
    def categories(self) -> Set[str]:
        return set(d['term'] for d in self.result['tags']) | set([self.category])

    @property
    def category(self) -> str:
        """Return the primary category."""
        return self.result['arxiv_primary_category']['term']

    @property
    def is_id_blacklisted(self):
        return self.url_id in config.URL_ID_BLACKLIST

    @property
    def is_id_whitelisted(self):
        return self.url_id in config.URL_ID_WHITELIST

    @property
    def is_title_whitelisted(self):
        """Return whether the title has one or more terms that are whitelisted."""
        return any(f' {term} ' in f' {self._title_cmp} ' for term in config.TERMS)

    @property
    def title(self) -> str:
        return self.result['title'].replace('\n ', '')

    @property
    def url_id(self) -> str:
        """Return the unique URL ID.

        Unlike `self.result['id']`, the URL ID is actually unique, especially for results older than 2007.
        """
        return self.result['arxiv_url'].replace('http://arxiv.org/abs/', '', 1).rsplit('v', 1)[0]

    @property
    def year_published(self) -> int:
        return self.result['published_parsed'].tm_year

    @property
    def year_updated(self) -> int:
        return self.result['updated_parsed'].tm_year

    @property
    def as_dict(self) -> Dict[str, Union[str, int]]:
        return {'URL_ID': self.result.url_id, 'Category': self.result.category, 'Title': self.title,
                'Year_Published': self.year_published, 'Year_Updated': self.year_updated}