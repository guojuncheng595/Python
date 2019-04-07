# -*- coding: utf-8 -*-
import scrapy


class YunpanjinglingSpider(scrapy.Spider):
    name = 'yunpanjingling'
    allowed_domains = ['https://www.yunpanjingling.com/']
    start_urls = ['http://https://www.yunpanjingling.com//']

    def parse(self, response):
        pass
