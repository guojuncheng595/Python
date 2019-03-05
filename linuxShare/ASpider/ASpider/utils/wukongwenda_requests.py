# -*- coding: utf-8 -*-
import requests
import bs4
from urllib.parse import urlencode
try:
    import cookielib
except:
    import http.cookiejar as cookielib

# import re
import json

# session = requests.session()
#
# agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
# header = {
#     "HOST":"www.yunpanjingling.com",
#     "User-Agent": agent,
#     "X-Requested-With": "XMLHttpRequest",
#     "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
#     "Content-Length": "48",
#     "Connection": "keep-alive",
#     "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Accept": "application/json, text/javascript, */*; q=0.01"
# }
#
#
# def get_cookies():
#     response = requests.get("https://www.yunpanjingling.com",headers=header)
#     if response.cookies:
#         for key, value in response.cookies.items():
#             return value
#     else:
#         return "none"
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

def ajaxRequest():

    headers = {
        "X-CSRF-TOKEN": "GDyx6XJQ6OajAmLC1D7PA9WbMXRswo1WqcS5u7Z2",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Cookie": "_ga=GA1.2.2102293619.1551623139; _gid=GA1.2.148598326.1551623139; XSRF-TOKEN=eyJpdiI6ImQzKzZocHJcL1pEMU9UWmZLaDE0YjhnPT0iLCJ2YWx1ZSI6Ind4WG5VWHVicEZyM2orcDlOYWlEWWplU2pqNENCTTgrRHhPenkrTkt4Rjdtc282UWlReEVqUHQzNmIydzdkRWpybWhUbjVpZzdkeGZzcWpjbnRZeExBPT0iLCJtYWMiOiIxYzc2NWUyOTY3OGQwNDllZTRiYTM0YjdhZjNmZGVlYjBkYmRkY2Y1ZTlkYTJlYjI5NDBkZTA5YjU0ODIyMmU3In0%3D; _session=eyJpdiI6InZWTTFJc0RvUTdJb2NuSUZOeTBhVmc9PSIsInZhbHVlIjoibGl1TnYwUW5wU1dDNW5halZjRmJkV0M0dW9MNktMbmNPUjg4akRLaHhXcEMzWDVjWlZtUzdDY1E4Uks2Z2haRVJtMSt3TGdTYjBadW5ZS2pOdTBuUlE9PSIsIm1hYyI6ImFjN2VkOTJjMzQ1MGM3NWE0OWY3MjE5OGRkNTk5MThkMjEzNWUyNjE2ZTk2OGY0MDVkMWMxYzE0NzlhY2U1NDIifQ%3D%3D; _gat_gtag_UA_109184535_5=1",
        "Host": "https://www.yunpanjingling.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0",
        "Content-Type": "application/json; charset=UTF-8"
    }
    # email=14124123512%40qq.com&password=sfasdd&remember=true
    datas = {'email': '2670617835@qq.com', 'password': 'g2670617835', 'remember': 'true'}
    # datas = {}
    # datas["email"] = "2670617835@qq.com"
    # datas["password"] = "g2670617835"
    # datas["remember"] = "true"

    url = "https://www.yunpanjingling.com/user/login"
    # session = requests.session()


    print(type(datas))
    print(type(json.dumps(datas)))
    requ = requests.post(url=url, data=json.dumps(datas), headers = headers)
    requ.encoding = "UTF-8"

    res = requ.text
    print(res)

ajaxRequest()