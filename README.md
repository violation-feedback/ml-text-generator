# The Garlic - Fake News headline generator

## Requirements

* Python 3
* markovify
* praw

## Usage

### Website

    python server.py [port]

### Sources

    python corpus.py download [subreddit]

e.g.

    python corpus.py download NotTheOnion

To set weights use the filename format `something.weight.txt` e.g. `worldnews.25.txt`. Default weight is 100.

## License

This work is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).