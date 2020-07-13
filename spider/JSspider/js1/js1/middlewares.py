# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver
from time import sleep
from scrapy.http.response.html import HtmlResponse

class Js1SpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class Js1DownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class SeleniumDownloadMiddleware(object):
    def __init__(self):
        self.browser=webdriver.Chrome(executable_path=r"D:\chromedriver80\chromedriver.exe")

    def process_request(self,request,spider):
        self.browser.implicitly_wait(2)
        self.browser.get(request.url)
        sleep(10)
        source=self.browser.page_source
        # try:
        #     count=0
        #     print("+"*100)
        #     while True:
        #         More=self.browser.find_element_by_xpath('//div[@class="continue-to-read"]/div/span[@class="moreBtn goBtn"]')
        #         print("+"*100)
        #         if More:
        #             print("找到了"*100,More)
        #             # More.click()
        #             self.browser.execute_script('arguments[0].click()',self.browser.find_element_by_xpath('//div[@class="continue-to-read"]/div/span[@class="moreBtn goBtn"]'))
        #             print("执行"*100)
        #             sleep(15)
        #             source=source+self.browser.page_source
        #             count+=1
        #             if count==1:
        #                 print(count)
        #                 break
        #         else:
        #             print("+没有匹配到"*10)
        #             break
        # except:
        #     pass
        # print("-"*100)
        # source=self.browser.page_source
        response=HtmlResponse(url=request.url,body=source,request=request,encoding="utf-8")
        return response
