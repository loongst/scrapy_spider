import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.options=webdriver.ChromeOptions()
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--ignore-ssl-errors')
        self.driver = webdriver.Chrome(chrome_options=self.options,executable_path=r"D:\chromedriver80\chromedriver.exe")

    def test_search_in_python_org(self):

        
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()



"""
import os
import sys,time
import selenium
from selenium import webdriver

driver = webdriver.Chrome(r"D:\chromedriver80\chromedriver.exe")

driver.get('https://wenku.baidu.com/view/f06abc274b35eefdc8d333b8.html?from=search')
time.sleep(30)
html = driver.page_source

print(html)
print('MMMMMMMMMMM')

time.sleep(10)
driver.close()

driver.quit()


import requests

url="https://wkbjcloudbos.bdimg.com/v1/docconvert1960/wk/1429053e5a20564732c8cb4f045b6d34/0.json?responseContentType=application%2Fjavascript&responseCacheControl=max-age%3D3888000&responseExpires=Thu%2C%2009%20Apr%202020%2016%3A06%3A33%20%2B0800&authorization=bce-auth-v1%2Ffa1126e91489401fa7cc85045ce7179e%2F2020-02-24T08%3A06%3A33Z%2F3600%2Fhost%2F49c9a70327d98cc6a9ae680ca3eeb1526749531b025678fae522d74fa3152aed&x-bce-range=0-14115&token=eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU4MjUzNTE5MywidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.JvXTqCMczw2%2BAnFL8MOTqYB8LpQL96K6JGvwvUEGPJU%3D.1582535193"

headers={
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Host': 'wkbjcloudbos.bdimg.com',
    'Referer': 'https://wenku.baidu.com/view/f06abc274b35eefdc8d333b8.html?from=search',
    'Sec-Fetch-Dest': 'script',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
}

resp=requests.request(method='get',url=url,headers=headers)
print(resp.text)
"""