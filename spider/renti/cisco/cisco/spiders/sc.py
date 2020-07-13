# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ScSpider(CrawlSpider):
    name = 'sc'
    allowed_domains = ['cisco.com']
    start_urls = ['https://software.cisco.com/download/home/284795752/type']

    rules = (
        Rule(LinkExtractor(allow=r'https://software.cisco.com/download/home/\d{9}/type/\d{9}/release/.*'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
