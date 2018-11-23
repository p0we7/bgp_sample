# BGP Crawler bots

## Installtion
---

```
$ pip install scrapy scrapy-splash
$ docker run -p 8050:8050 scrapinghub/splash
```

## Configure
---

Modify `SPLASH_URL` in `settings.py` to you IP Address.

> SPLASH_URL = 'http://192.168.99.100:8050'

## Usage
---

Run spider
```
$ cd bgp_bots
$ scrapy crawl BGPSpider -o BGP.json
```
