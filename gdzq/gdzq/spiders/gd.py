import scrapy


class GdSpider(scrapy.Spider):
    name = 'gd'
    allowed_domains = ['finance.sina.com.cn']
    start_urls = ['http://finance.sina.com.cn/realstock/company/sh601788/nc.shtml?from=BaiduAladin']

    def parse(self, response):
        pass
