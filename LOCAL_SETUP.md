# Odds downloader configuration

The original SportsArb code remains Akash Khanna's project. `jsonDownload.py` now reads its key from the `ODDS_API_KEY` environment variable instead of a source literal.

Install the script's `requests` dependency in your virtual environment. Copy `.env.example` to `.env`, fill in your own key locally, and export it before running:

```sh
set -a
source .env
set +a
python jsonDownload.py
```

`.env` does not load automatically and must stay out of Git. Running the downloader makes a live API request, uses your provider quota, and writes `odds_data.json` in the current directory. Missing/empty configuration fails before a request. The existing v3 endpoint, sport, region, parsing, and output behavior are preserved; service/API compatibility has not been validated.

The user reports the exposed key is revoked; no key was tested. Removing a current source literal does not revoke it or remove it from Git history. No history rewrite or live requests were performed.

Run the configuration regression tests without dependencies or network:

```sh
python3 -m unittest discover -s tests -v
```
