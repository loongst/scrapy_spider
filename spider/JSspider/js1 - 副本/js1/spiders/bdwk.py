# -*- coding: utf-8 -*-
import scrapy


class BdwkSpider(scrapy.Spider):
    name = 'bdwk'
    allowed_domains = ['wenku.baidu.com']
    start_urls = ['https://wenku.baidu.com/view/7206c77e14791711cc791779.html?from=search']

    def parse(self, response):
        pass
