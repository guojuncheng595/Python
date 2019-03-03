# -*- coding: utf-8 -*-
import requests

try:
    import cookielib
except:
    import http.cookiejar as cookielib

import re

session = requests.session()

agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
header = {
    "HOST":"www.yunpanjingling.com",
    "User-Agent":agent
}

def get_csrf():
    # 获取csrf code   https://www.jianshu.com/p/887af1ab4200
    response = requests.get("https://www.yunpanjingling.com",headers=header)



    # print(response.text) #获取服务器获取的值
    # text = '<meta name="csrf-token" content="96Q2Z4fe8mEbudMOxaQUR2tRZMPRczCSci20AYuQ" />'
    match_obj = re.match('.*name="csrf-token" content="(.*?)"', response.text)
    if match_obj:
        print(match_obj.group(1))
    else:
        return "none"


def wukongwenda_login(account,password):
    header = {
        "HOST": "www.yunpanjingling.com",
        "User-Agent": agent,
        "Cookie":Cookie
    }

    # 悟空问答 - 登陆
    if re.match("[0-9a-zA-Z_]{0,19}@qq.com",account):
        print("手机号码登陆")
        post_url = "https://www.yunpanjingling.com/user/login"
        post_date = {
            # "test":get_ccid,
            # "remember": "true",
            "email": account,
            "password": password
        }
        response_text = session.post(post_url,data=post_date,headers=header)
        print(response_text)
        session.cookies.save()


wukongwenda_login("2670617835@qq.com","g2670617835")
# get_csrf()

