'''
Created on 2018/06/29

@author: yangpn
'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import scrapy
import urllib
import os
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector

class XiaoHuarSpider(scrapy.Spider):
    '''
    classdocs
    '''
    name = "xiaohuar"
    allowed_domains = ["amazon.co.jp"]
    start_urls = [
        "https://www.amazon.co.jp/gp/product/B07D28N3GR"
    #    ,"https://www.amazon.co.jp/gp/product/B011QBM8EM/ref=s9_acsd_zgift_hd_bw_bBVy8B_c_x_w?pf_rd_m=AN1VRQENFRJN5&pf_rd_s=merchandised-search-4&pf_rd_r=KWAVGJ9MTK9S6J4X2677&pf_rd_t=101&pf_rd_p=0f7681be-fdca-57d7-bbba-0fa6a16d6165&pf_rd_i=170159011"
    ]

    def parse(self, response):
        # print(response, type(response))
        # from scrapy.http.response.html import HtmlResponse
        # print(response.body_as_unicode())
#         unicode_body = response.body
        
        hxs = scrapy.Selector(response)
        
        #urllib.urlretrieve(path2[0], "D:/img/" + "aaa.jpg")
        alt  = hxs.xpath('//div[@id="imgTagWrapperId"][@class ="imgTagWrapper"]/img/@alt').extract_first().encode('utf-8')
        price = hxs.xpath("//span[@id='priceblock_ourprice']/text()").extract_first().encode('utf-8')
#         file_path = os.path.join("c:/aa/")
        detail = hxs.xpath("//div[@id='productDescription_feature_div']/div[@id='productDescription']/p[1]").extract_first().encode('utf-8')
        
        
        
        str1 = price.replace(",", "")
        str2 = str1[4:]
        detail = detail.replace("<br>", "",9)
        detail = detail.replace("<p>", "",19)
        detail = detail.replace("</p>", "",19)
        
        path2 = hxs.xpath('//div[@id="imgTagWrapperId"][@class ="imgTagWrapper"]/img/@src').extract_first().encode('utf-8')
        #-->https://images-na.ssl-images-amazon.com/images/I/81rpx-IyHRL._AC_UL115_.jpg
        
        itemo = path2.split("/")
        filename = itemo[len(itemo) - 1] #-->81rpx-IyHRL._AC_UL115_.jpg
        
        array1 = filename.split("_") 
        
        
        newname = array1[0] 
        start = path2.find(filename)
        newpath = path2[0 : start] + newname + "jpg"
        
        
        
        folder = newname
        
        if not os.path.exists('D:/img/'+ newname) :
            os.mkdir('D:/img/'+ folder)
        urllib.urlretrieve(newpath, 'D:/img/'+ folder+ "/" + filename)
        f = open('D:/img/'+ folder +'/sample.txt', 'w')
        print >> f, int(int(str2) * 0.06)
        print >> f, str2
        print >> f, detail
        print >> f, alt
        print >> f, newpath
        #print >> f, "path2 : " + array1[1] + array1[2]
        print >> f, "path2 : " + path2
        
        
#         for i in range(len(path2)):
#             path = path2[i].encode('utf-8');
# #             alt = path2[i].xpath('@alt').extract_first().encode('utf-8')
#            
#             #itemo = path.split("/")
#             #filename = itemo[len(itemo)-1]
#             #urllib.urlretrieve(path, "D:/img/" +  path2[i].xpath('@alt').extract_first() +".jpg")
#             print >> f, path
# #             print >> f, alt
#             #print >> f, alt[i]
#             
#         f.close()
        
#         print >> f, path
        
        
        
        