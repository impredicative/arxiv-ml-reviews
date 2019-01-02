# arxiv-ml-reviews
This uses a [keyword](arxivmlrev/_config/terms.csv)-based search to extract a list of review articles from
[arXiv's](https://arxiv.org/) various [categories](arxivmlrev/_config/categories.txt)
on machine learning and artificial intelligence.

The code is admittedly research-grade; it is currently not polished for general use.

## Requirements
* Python 3.7+
* In a new virtual environment or container, run the following, falling back to the versioned `requirements.txt` instead
if there are any issues.
```
pip install -U pip
pip install -r requirements.in
```

## Usage
1. Run `python ./arxivmlrev/searcher.py`. This is expected to rewrite the file `data/articles.csv`.
For better or worse, the script currently refreshes the entire file, and doesn't just update the latest results.
Use git to check if the diff of this updated CSV file looks acceptable.
If the CSV file is smaller for any reason, it means the search query failed, in which case it should be rerun.
**As a warning, this step should not be run excessively** as it burdens the arXiv search server.

1. If there is any extraneous new entry in `data/articles.csv`, update either `arxivmlrev/_config/articles.csv` and/or
`arxivmlrev/_config/terms.csv` with a new blacklist entry. This is expected to be be done rarely.
Blacklisted entries are those with *Presence* = 0.
Before committing these updated configuration files to revision control, consider running
`scripts/sort_config_articles.py` and/or `scripts/sort_config_terms.py` respectively.
If a configuration file was updated, rerun the prior search step.

1. If the updated `data/articles.csv` looks good, a markdown version of it, i.e. `data/articles.md`, can be generated by
running `scripts/write_md.py`.

1. If the generated `data/articles.md` looks good, it can be published to GitHub by running `scripts/publish_md.py`.
This requires GitHub-specific configuration in `config.py`.

## To do
* Improve code quality.
* By default, run an incremental update, and provide an option to do a full rerun.
An incremental update assumes an unchanged configuration.
This also require changing the code to sort the results by *lastUpdatedDate* rather than by *submittedDate*.