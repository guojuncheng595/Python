# -*- coding: utf-8 -*-
import scrapy
# import re
# import sys

class YunPan(scrapy.Spider):
    name = 'yunpan'
    allowed_domains = ['www.yunpanjingling.com']

    start_urls = ['https://www.yunpanjingling.com/search/python']
    def parse(self, response):

        post_nodes = response.css(".search-list a::text").extract()
        print(post_nodes)

        pass