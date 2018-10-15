# -*- coding: utf-8 -*-
import scrapy
import re

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/114442/']

    def parse(self, response):
        # /html/body/div[3]/div[3]/div[1]/div[1]/h1
        # /html/body/div[1]/div[3] div[1]/div[1]/h1
        # re_selector = response.xpath("/html/body/div[1]/div[3] div[1]/div[1]/h1")
        # // *[ @ id = "post-114440"] / div[1] / h1
        # re2_selector = response.xpath('//*[@id="post-114440"]/div[1]/h1/text()')

        title = response.xpath('//*[@id="post-114440"]/div[1]/h1/text()').extract()[0]

        create_date = response.xpath('//*[@id="post-114440"]/div[2]/p/text()').extract()[0].strip().replace(".","").strip()

        fav_nums = response.xpath("//span[contains(@class,'bookmark-btn')]/text()").extract()[0]
        match_re = re.match(".*(\d+).*",fav_nums)
        if match_re:
            fav_nums = match_re.group(1)

            tag_list = response.xpath("//p[@class='entry-meta-hide-on-mobile']/a/text()").extract()


        pass
