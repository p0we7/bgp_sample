# -*- coding: utf-8 -*-

# Scrapy settings for bgp_bots project
#

BOT_NAME = 'bgp_bots'

SPIDER_MODULES = ['bgp_bots.spiders']
NEWSPIDER_MODULE = 'bgp_bots.spiders'

SPLASH_URL = 'http://192.168.99.100:8050'
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'


USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
ROBOTSTXT_OBEY = True

SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
