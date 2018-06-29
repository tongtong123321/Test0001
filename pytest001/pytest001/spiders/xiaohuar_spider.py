'''
Created on 2018/06/29

@author: yangpn
'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import scrapy

class XiaoHuarSpider(scrapy.Spider):
    '''
    classdocs
    '''
    name = "xiaohuar"
    allowed_domains = ["xiaohuar.com"]
    start_urls = [
        "http://www.xiaohuar.com/hua/"
    ]

    def parse(self, response):
        # print(response, type(response))
        # from scrapy.http.response.html import HtmlResponse
        # print(response.body_as_unicode())
        unicode_body = response.body
        f = open('c:\\aa\\sample.txt', 'w')
        print >> f, unicode_body
        f.close()
        
        
        
        