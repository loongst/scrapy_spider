# -*- coding: utf-8 -*-
import scrapy
import json
from js1.items import Js1Item
class BdwkSpider(scrapy.Spider):
    name = 'bdwk'
    allowed_domains = ['wenku.baidu.com']
    start_urls = ['https://wkbjcloudbos.bdimg.com/v1/docconvert8542/wk/2547e53d9b80aea6ece7e47ed54b158d/0.json?responseContentType=application%2Fjavascript&responseCacheControl=max-age%3D3888000&responseExpires=Wed%2C%2013%20May%202020%2012%3A43%3A03%20%2B0800&authorization=bce-auth-v1%2Ffa1126e91489401fa7cc85045ce7179e%2F2020-03-29T04%3A43%3A03Z%2F3600%2Fhost%2F775ee9a300e011115e9a28e7d437a31a0150134755d65a90bff94ecf9a88ccfa&x-bce-range=0-6502&token=eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU4NTQ2MDU4MywidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.DbBDx6uB0j5zXrU54sy4jFROQfvPoq0cQTSR4jx5ok4%3D.1585460583']
    # https://wenku.baidu.com/view/7206c77e14791711cc791779.html?from=search
    # https://wenku.baidu.com/view/90cba7a9185f312b3169a45177232f60dccce706.html?from=search

    def parse(self, response):
        with open("ppp.html","w",encoding="utf-8") as f:
            f.write(response.text)
        # content=response.xpath('//div[@class="reader-txt-layer"]//p/text()').getall()
        # print(content)
        # item=Js1Item()
        # content=''.join(content)
        # item['content']=content
        item=json.loads(response.text)
        return item
