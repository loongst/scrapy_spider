# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver



class JstestSpider(scrapy.Spider):
    name = 'jstest'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):

        browser = webdriver.chrome()
        browser.get()

        pass
