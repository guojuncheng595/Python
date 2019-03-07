# -*- coding: utf-8 -*-
import requests
try:
    import cookielib
except:
    import http.cookiejar as cookielib

import re
import json
import bs4
from requests.cookies import RequestsCookieJar

session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename='cookies')
session.cookies.save(ignore_discard=True)
try:
    session.cookies.load(ignore_discard=True)
except:
    print("Cookie 未能加载")

#
#

#
#

#
#
# def get_csrf():
#     # 获取csrf code   https://www.jianshu.com/p/887af1ab4200
#     response = requests.get("https://www.yunpanjingling.com", headers=header)
#     soup = bs4.BeautifulSoup(response.text, "html.parser")
#     soup.title.string[3:7]
#     for meta in soup.select('meta'):
#         if meta.get('name') == 'csrf-token':
#             return meta.get('content')
#     # print(meta.get('content'))
#     # print(response.text) #获取服务器获取的值
#     # text = '<meta name="csrf-token" content="96Q2Z4fe8mEbudMOxaQUR2tRZMPRczCSci20AYuQ" />'
#     # match_obj = re.match('.*name="csrf-token" content="(.*?)"', response.text)
#     # if match_obj:
#     #     return (match_obj.group(1))
#     # else:
#     #     return "none"
#
#
# def wukongwenda_login(account, password):
#     header = {
#         "HOST": "www.yunpanjingling.com",
#         "User-Agent": agent,
#         "Cookie": get_cookies(),
#         "X-CSRF-TOKEN": get_csrf()
#     }
#
#     # 悟空问答 - 登陆 ; 1551623139
#     if re.match("[0-9a-zA-Z_]{0,19}@qq.com", account):
#         print("手机号码登陆")
#         post_url = "https://www.yunpanjingling.com/user/login"
#         post_date = {
#             # "test":get_ccid,
#             "email": account,
#             "password": password,
#             "remember": "true"
#         }
#         response_text = session.post(post_url, data=post_date)
#         print(response_text.text)
#         # session.cookies.save()


# wukongwenda_login("2670617835@qq.com", "g2670617835")
# get_csrf()

header = {
    "HOST":"www.yunpanjingling.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Accept": "application/json, text/javascript, */*; q=0.01"
}

def get_xsrf_token():
    response = requests.get("https://www.yunpanjingling.com/user/login", headers=header)
    token = ""
    if response.cookies:
        for key, value in response.cookies.items():
            if key == 'XSRF-TOKEN':
                token += ("XSRF-TOKEN=" + value + ";")
            elif key == '_session':
                token += ("_session=" + value + ";")
        print(token[:-1])
        return token[:-1]
    else:
        return "none"

def get_csrf_token():
    # 获取csrf code   https://www.jianshu.com/p/887af1ab4200
    response = requests.get("https://www.yunpanjingling.com/user/login", headers=header)

    token = ""
    ctoken = ""
    if response.cookies:
        cookie_jar = RequestsCookieJar()
        cookie_jar.set("BAIDUID", "B1CCDD4B4BC886BF99364C72C8AE1C01:FG=1", domain="baidu.com")
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
    ctoken = "none"
    for meta in soup.select('meta'):
        if meta.get('name') == 'csrf-token':
            print(meta.get('content'))
            ctoken = meta.get('content')
    return [ctoken, token]


def ajaxRequest():
    headers = {
        "X-CSRF-TOKEN": get_csrf_token()[0],
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Cookie": get_csrf_token()[1],
        "Content-Type": "application/json; charset=UTF-8"
    }
    datas = {'email': '2670617835@qq.com', 'password': 'g2670617835', 'remember': 'true'}
    url = "https://www.yunpanjingling.com/user/login"
    response = session.post(url=url, data=json.dumps(datas), headers=headers)
    if response.status_code == 200:
        print("返回码：" + str(response.status_code))
    else:
        print("返回码：" + str(response.status_code))
    session.cookies.save()
    cookie = session.cookies
    print(cookie)


ajaxRequest()
# test = get_csrf_token()
# print(test[0])
# print(test[1])
# get_xsrf_token()

# get_csrf_token()