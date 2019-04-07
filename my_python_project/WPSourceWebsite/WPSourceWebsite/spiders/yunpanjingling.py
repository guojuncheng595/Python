# -*- coding: utf-8 -*-
import re
import scrapy

from WPSourceWebsite.items import WPItemLoader, WPSearchItem

try:
    import cookielib
except:
    import http.cookiejar as cookielib


header = {
    "HOST": "www.yunpanjingling.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Accept": "application/json, text/javascript, */*; q=0.01"
}


class YunpanjinglingSpider(scrapy.Spider):
    name = 'yunpanjingling'
    allowed_domains = ['https://www.yunpanjingling.com/']
    start_urls = ['https://www.yunpanjingling.com/search/python']

    def parse(self, response):
        item_loader = WPItemLoader(item=WPSearchItem(), response=response)
        titles = response.css('div.search-list')
        for title in titles:

            t_title = title.css("div.name a")
            # 获取内容详情的url
            title_url = t_title.css("::attr(href)").extract_first("")
            print('标题url：title_url:' + title_url)
            # 获取内容title
            rex = '<a.*?href="(.+)".*?>(.*?)</a>'
            match_re = re.match(rex, t_title.extract_first(""))
            print('标题title:' + match_re.group(2).strip().replace("<em>", "").replace("</em>", ""))
            # 获取内容副标题
            s_title = title.css("div.referrer a")
            # 获取内容的来源网站 TODO 可能为空
            s_title_url = s_title.css("::attr(href)").extract_first("")
            print("来源网址url：" + s_title_url)
            # 副标题内容
            match_re = re.match(rex, s_title.extract_first(""))
            print('副标题内容s_title:' + match_re.group(2).strip().replace("<em>", "").replace("</em>", ""))


        # item_loader.add_css("title", "div.search-list div.name")
        pass
