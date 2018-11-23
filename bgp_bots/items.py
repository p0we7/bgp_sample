# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy



class ASNItem(scrapy.Item):
    company = scrapy.Field()
    as_number = scrapy.Field()
    ipv4_range = scrapy.Field()
    ipv6_range = scrapy.Field()

class DomainItem(scrapy.Item):
    domain = scrapy.Field()
    record_type = scrapy.Field()
    ip = scrapy.Field()
    checked = scrapy.Field()
    