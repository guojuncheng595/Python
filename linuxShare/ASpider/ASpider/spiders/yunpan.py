# -*- coding: utf-8 -*-
import scrapy
import bs4
import requests
try:
    import cookielib
except:
    import http.cookiejar as cookielib
# import re
# import sys
session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename='cookies.txt')
session.cookies.save(ignore_discard=True)
try:
    session.cookies.load(ignore_discard=True)
except:
    print("Cookie 未能加载")

header = {
    "HOST":"www.yunpanjingling.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Accept": "application/json, text/javascript, */*; q=0.01"
}

class YunPan(scrapy.Spider):

    name = 'yunpan'
    allowed_domains = ['www.yunpanjingling.com']

    start_urls = ['https://www.yunpanjingling.com/search/python']
    def parse(self, response):

        post_nodes = response.css(".search-list a::text").extract()
        print(post_nodes)

    def start_requests(self):
        return [scrapy.Request('https://www.yunpanjingling.com/user/login', headers=header, callback=self.login,dont_filter=True)]

    def login(self,response):
        # response = requests.get("https://www.yunpanjingling.com/user/login", headers=header)
        token = ""
        ctoken = "none"
        if response.cookies:
            for key, value in response.cookies.items():
                if key == 'XSRF-TOKEN':
                    token += ("XSRF-TOKEN=" + value + ";")
                elif key == '_session':
                    token += ("_session=" + value + ";")
            print(token[:-1])
            token = token[:-1]
        else:
            token = 'none'

        soup = bs4.BeautifulSoup(response.text, "html.parser")
        soup.title.string[3:7]
        for meta in soup.select('meta'):
            if meta.get('name') == 'csrf-token':
                print(meta.get('content'))
                ctoken = meta.get('content')
        # return [ctoken, token]
        if ctoken and token:
            headers = {
                "X-CSRF-TOKEN": ctoken,
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "Cookie": token,
                "Content-Type": "application/json; charset=UTF-8"
            }
            post_data = {
                'email': '2670617835@qq.com',
                'password': 'g2670617835',
                'remember': 'true'
            }
            post_url = "https://www.yunpanjingling.com/user/login"

            return [scrapy.FormRequest(
                url=post_url,
                formdata=post_data,
                headers=headers,
                callback=self.check_login
            )]

    def check_login(self, response):
        # 验证服务器的返回数据判断是否成功
        pass


