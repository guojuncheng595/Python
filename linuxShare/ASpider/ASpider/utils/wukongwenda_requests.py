# -*- coding: utf-8 -*-
import requests

try:
    import cookielib
except:
    import http.cookiejar as cookielib

import re

agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
header = {
    "HOST":"www.yunpanjingling.com",
    "User-Agent":agent
}

def get_ccid():
    response = requests.get("https://www.yunpanjingling.com",headers=header)
    print(response.text) #获取服务器获取的值
    return ""



def wukongwenda_login(account,password):
    # 悟空问答 - 登陆
    if re.match("^1\d{10}",account):
        print("手机号码登陆")
        post_url = "https://www.yunpanjingling.com/user/login"
        post_date = {
            # "test":get_ccid,
            "remember": "true",
            "email": account,
            "password": password
        }

get_ccid()

