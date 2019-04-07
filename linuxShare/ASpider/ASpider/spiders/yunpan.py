# -*- coding: utf-8 -*-
import scrapy.http.request
import bs4
import requests
import json

from requests import Request
from scrapy.http.cookies import CookieJar    # 该模块继承自内置的http.cookiejar,操作类似
# 实例化一个cookiejar对象
cookie_jar = CookieJar()
try:
    import cookielib
except:
    import http.cookiejar as cookielib
import re
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
        return [scrapy.http.Request('https://www.yunpanjingling.com/user/login', meta={'cookiejar': 1}, headers=header, callback=self.login)]

    def login(self, response):
        # 如果有图片验证码
        # import time
        # t = str(int(time.time()*1000))
        # captcha_url = ""
        # yield scrapy.Request(captcha_url, headers=self.headers, meta={"post_data":post_data},callback=self.login_after_captcha)
        #


        # https://www.jianshu.com/p/404e4ac156a6
        cookies = response.headers.getlist('Set-Cookie')
        print("后台首次写入，相应的Cookies", cookies)
        str_cookies = ""
        for cookie in cookies:
            # https://www.cnblogs.com/timelesszhuang/p/7235798.html
            str_cookie = re.findall(r"(.*?) expires", str(cookie, encoding="utf-8"))
            str_cookies += str_cookies.join(str_cookie)
            print("序号：%s 值：%s"%(cookie.index(cookie)+1, str_cookie))
        print("合成后的cookie的值为：", str_cookies[:-1])

        # 获取x-csrf-token值
        ctoken = "none"
        soup = bs4.BeautifulSoup(response.text, "html.parser")
        soup.title.string[3:7]
        for meta in soup.select('meta'):
            if meta.get('name') == 'csrf-token':
                print(meta.get('content'))
                ctoken = meta.get('content')
        # return [ctoken, token]
        if ctoken and str_cookies:
            headers = {
                "X-CSRF-TOKEN": ctoken,
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "Cookie": str_cookies,
                "Content-Type": "application/json; charset=UTF-8"
            }
            post_data = {
                'email': '2670617835@qq.com',
                'password': 'g2670617835',
                'remember': 'true'
            }
            post_url = "https://www.yunpanjingling.com/user/login"
            response = session.post(url=post_url, data=json.dumps(post_data), headers=headers)
            if response.status_code == 200:
                print("返回码：" + str(response.status_code))
                print("返回码：" + str(response.text.encode("utf-8")))
                self.check_login(response)
            else:
                test = str(response.text.encode("utf-8"))
                print("返回码：" + test)
            session.cookies.save()


    def check_login(self, response):
        # 验证服务器的返回数据判断是否成功
        pass

    # 图形验证码获取
    def login_after_captcha(self,response):
        with open("captcha.jpg","wb") as f:
            f.write(response.body)
            f.close()
        from PIL import Image
        try:
            im = Image.open('captcha.jpg')
            im.show()
            im.close()
        except:
            pass
        captcha = input("输入验证码\n>")
        # 登陆URL
        post_url = ""
        # 登陆请求数据
        post_data = response.meta.get("post_data",{})
        post_data["captcha"] = captcha
        # 验证服务器返回的数据是否成功
        text_json = json.load(response.txt)
        if "msg" in text_json and text_json["msg"] == "登陆成功":
            for url in self.start_urls:
                yield scrapy.Request(url,dont_filter=True)







