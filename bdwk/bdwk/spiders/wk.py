# -*- coding: utf-8 -*-
import scrapy

from time import sleep
class WkSpider(scrapy.Spider):
    name = 'wk'
    # allowed_domains = ['wenku.baidu.com']
    start_urls = ['http://httpbin.org/user-agent']

    def parse(self, response):
        # print(response.body)
        
        sleep(5)
        yield scrapy.Request(url=response.url,callback=self.parse,dont_filter=True)
        pass
