# -*- coding: utf-8 -*-
import scrapy


class MyqzSpider(scrapy.Spider):
    name = 'myqz'
    allowed_domains = ['http://192.168.1.66/w3c/www.w3cschool.cc/']
    start_urls = ['http://http://192.168.1.66/w3c/www.w3cschool.cc//']

    def parse(self, response):
        pass
