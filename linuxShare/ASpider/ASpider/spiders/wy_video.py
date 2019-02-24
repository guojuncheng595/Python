# -*- coding: utf-8 -*-
import scrapy
import re
# import sys

class WanYingVideo(scrapy.Spider):
    name = 'sodyy'
    allowed_domains = ['www.sodyy.com']

    start_urls = ['http://www.sodyy.com/vod-type-id-1-pg-1.html']
    def parse(self, response):

        post_nodes = response.css(".movie-name::text").extract()
        for post_node in post_nodes:
            print("序号：%s，值：%s" % (post_nodes.index(post_node) + 1,post_node))

        pass