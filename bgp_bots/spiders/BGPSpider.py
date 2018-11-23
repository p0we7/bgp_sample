# -*- coding: utf-8 -*-

import os
import scrapy
from scrapy_splash import SplashRequest

lua_script = """
function main(splash)
  --splash:set_user_agent(splash.args.ua)
  assert(splash:go(splash.args.url))

  -- requires Splash 2.3
  while not splash:select('#search') and not splash:select('#whois') do
    splash:wait(1)
  end
   return {
    html = splash:html(),
    cookies = splash:get_cookies(),
  }
end
"""
class BgpspiderSpider(scrapy.Spider):
    name = 'BGPSpider'
    allowed_domains = ['bgp.he.net']
    urls = [
        'https://bgp.he.net/AS395354',
        'https://bgp.he.net/search?search%5Bsearch%5D=starry&commit=Search'
        ]

    cookies = []
    def start_requests(self):
            yield SplashRequest(
                url=self.urls[0],
                callback=self.parse,
                endpoint='execute',
                args={
                    'lua_source': lua_script
                }
            )
            yield SplashRequest(
                url=self.urls[1],
                callback=self.parse_search,
                endpoint='execute',
                args={
                    'lua_source': lua_script
                }
            )

    def _save_resopnse_to_html(self, response):

        if 'search' in response.url:
            file_name = 'SEARCH_detail.html'
        else:
            file_name = 'ASN_detail.html'

        file_name = './data/' + file_name
        
        os.makedirs(os.path.dirname(file_name), exist_ok=True)
        with open(file_name, 'w') as f:
            f.write(response.body.decode('utf-8'))


    def parse(self, response):
        # 9 item
        next_request = []
        self.logger.debug('on parse ASN, URL %s', response.url)

        self._save_resopnse_to_html(response)

        if not self.cookies:
            self.cookies = response.data['cookies']

        as_number = response.xpath('//h1/a/text()').re(r'AS\d+')[0]
        table = response.xpath('//*[@id="table_prefixes4"]/tbody/tr')
        for row in table:
            next_request.append(response.urljoin(row.xpath('./td[1]/a/@href').extract_first()))


        self.logger.debug('Have %d domain item need crawl on AS', len(next_request))


    def parse_search(self, response):
        # 13 item

        next_request = []
        self.logger.debug('on parse SEARCH, URL %s', response.url)
        companys = ['Starry, Inc.']

        table = response.xpath('//*[@id="search"]/table/tbody/tr')
        self.logger.debug(table)

        self._save_resopnse_to_html(response)

        for row in table:

            ip = row.xpath('./td[1]/a/text()').extract_first()
            company_name = row.xpath('./td[2]/text()').extract_first()

            try:
                if company_name in companys:
                    self.logger.debug('Company name is %s', company_name)
                    next_request.append(response.urljoin(row.xpath('./td[1]/a/@href').extract_first()))
                else:
                    continue
            except Exception as e:
                self.logger.debug(e)
                continue


        self.logger.debug('Have %d domain item need crawl on SEARCH', len(next_request))