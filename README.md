# line_bot

### A focused web crawler (bot) that collects lines for each game of each sport for A.I. Sports

This repository holds all the necassary components to run a Scrapy web crawler on the [Sports Book Review](https://www.sportsbookreview.com/betting-odds/) website. The scraper is currently configured to write the documents to a JSON file called "items.jl".

The program can be run by running the following in the command line:

```bash
git clone https://github.com/a-i-sports/line_bot.git
cd line_bot
pip install -r requirements.txt
python release_spiders.py
```
