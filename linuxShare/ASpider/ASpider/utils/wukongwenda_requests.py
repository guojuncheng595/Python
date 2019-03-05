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
    # url = "https://www.yunpanjingling.com/user/login"
    # para = {"email": "2670617835@qq.com", "password": "g2670617835", "remember": True}
    # headers = {}
    # r = requests.post(url, data=json.dumps(para), headers=headers).text
    # print(r)
    # # print('get请求获取的响应结果json类型', r.text)
    # # print("get请求获取响应状态码", r.status_code)
    # # print("get请求获取响应头", r.headers['Content-Type'])
    # # 响应的json数据转换为可被python识别的数据类型
    # # json_r = r.json()
    # # print(json_r)

    headers = {
        'Host': 'www.yunpanjingling.com',
        'Referer': 'https://www.yunpanjingling.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'}
    # headers = {
    #     "csrf-token": "oHdZHZBaV67q43Jda112ANwysN7hMnxarh9ZyoGD",
    #     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    #     "Accept-Encoding": "gzip, deflate, br",
    #     "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    #     "Cache-Control": "max-age=0",
    #     "Connection": "keep-alive",
    #     "Cookie": "_ga=GA1.2.1706449788.1550903179; _gid=GA1.2.634801630.1551624876; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IlM1ZDlFeTNtMkdcL1VrYXdrUnVneXFBPT0iLCJ2YWx1ZSI6IitLNERHZGYyWjVKR3d4VURFcmlsbmVWZTNFR0NaZ01Zdzk3S3RXcDdTbWhtMG9uSklzYlk5U1V1MkY4aUJ0OG5lZXA3d2Q5V1ZOZHVnaDFBWGlZWWdwYWNDUldWbmYzQW44Q1pjVDhIYkRsdGgyQSt5U1hKU3p6QUkwOHpnUU82M0FSOVdCR0E1VHZNSVlnblFpQ2NuNFRUakJheG9CakE2cFB0ZlJMYjRJR3lLTUxqSVdhOXQ2dFpQWGFyaGZpSGRxNUJBN1lDVlA4MjBwTHl0TTArdUE9PSIsIm1hYyI6IjJjMTBiNWZlNmI4MWNmYzU5ZTFiYTlhOTliZGI5N2NmOTdhN2ViOGI0YWIzZjViZDg3MGQ1MzUzOWZkMzM3M2IifQ%3D%3D; XSRF-TOKEN=eyJpdiI6InowM3RxdmF2disxVlNwaCtXQklsaWc9PSIsInZhbHVlIjoiVFBMSXRJYTVVeURONFl1UHgxa0pwZk02R1BCVVRENUd5QW04dWlPeFNoZ2pwQ3lPMTJSazdtYnNxU2RvbzRNOVwvMFlvNnNiRVBjZkNlTGwrZnFzSWhnPT0iLCJtYWMiOiIwNzA2MzEwMWRkMWUxN2JjNjNlODllOGI5MzYyMzFkODIwZjY3MDU2NzMyMzYzOTllNWYyNjRkNDNiN2M5ZTM2In0%3D; _session=eyJpdiI6IkFGOFR1TGZBdkgxXC80N2pTc1BteU1RPT0iLCJ2YWx1ZSI6InRvc0Rzb2JhdGp6bHVBbDhuTVwvNlA2dWNrOGRMUXBIZjFvRjhKZVYwaHJuVHVBdnBNZlpxdis1YWR2Uyt2blNPeW81Q2xBbGNCWGVkK09iTzJCWER6UT09IiwibWFjIjoiOWNmMDk3NDgyZjM2OWE2Yjg1M2U5OTIzMWE1MzRhYzRhNWY0OWMzZjQ5NTkyMDc4Y2E4NTAxZTZkZjBjOWVkOSJ9; _gat_gtag_UA_109184535_5=1",
    #     "Host": "https://www.yunpanjingling.com",
    #     "Upgrade-Insecure-Requests": "1",
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36",
    #     'Content-Type': 'application/json'
    # }

    cookies = {
        "Cookie":"_ga=GA1.2.1706449788.1550903179; _gid=GA1.2.634801630.1551624876; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IlM1ZDlFeTNtMkdcL1VrYXdrUnVneXFBPT0iLCJ2YWx1ZSI6IitLNERHZGYyWjVKR3d4VURFcmlsbmVWZTNFR0NaZ01Zdzk3S3RXcDdTbWhtMG9uSklzYlk5U1V1MkY4aUJ0OG5lZXA3d2Q5V1ZOZHVnaDFBWGlZWWdwYWNDUldWbmYzQW44Q1pjVDhIYkRsdGgyQSt5U1hKU3p6QUkwOHpnUU82M0FSOVdCR0E1VHZNSVlnblFpQ2NuNFRUakJheG9CakE2cFB0ZlJMYjRJR3lLTUxqSVdhOXQ2dFpQWGFyaGZpSGRxNUJBN1lDVlA4MjBwTHl0TTArdUE9PSIsIm1hYyI6IjJjMTBiNWZlNmI4MWNmYzU5ZTFiYTlhOTliZGI5N2NmOTdhN2ViOGI0YWIzZjViZDg3MGQ1MzUzOWZkMzM3M2IifQ%3D%3D; XSRF-TOKEN=eyJpdiI6Ik9jbWsrdTczb3hBOFdvaU9SV2VPTHc9PSIsInZhbHVlIjoib3BSXC9menNzTXVMR05jZ3o3dElMcTBkS09USCtKSmdEaXRiMUJ1K1N3M3NaUFRRM1ZKbUJCYmdDbE0xZDRqem5tbkc1RXBlTmxhdERRRXVyOTl6TFFBPT0iLCJtYWMiOiJmNWVkNjI4MjJkMGU0MGQ2ZDE3ZDYwOTM1NmRlZDEyYzZjM2ZkNTc3ZDllZGNmZDJiMzY2ZTc4ZmU2Yjg0YWZkIn0%3D; _session=eyJpdiI6IlhVSTRKZGt5QTJ0b2o0cTREQis3YVE9PSIsInZhbHVlIjoiYzRCRVU4ZzA3TEJGZkFwbXBqYWlSbjVLakFBVUo1UGk1b1RlTkVVaWk1ZG5YR1hEYmhxeGxISkNQRFdpYVwvaGg2Y1dUditWSHNtcVMybzhjMkkzUUdRPT0iLCJtYWMiOiIxZDRlMTVlZGM1Y2UyNmMzMTdmZjVmZWMzM2M5ZWY5YjU2MTlhODY0MWQ0YzEzY2Q5MWY4YmZmNjBlNTcxYmQyIn0%3D; _gat_gtag_UA_109184535_5=1"
    }

    # datas = {
    #     'conditions': '{"city_code":"440100","hid":-1,"capacity":-1,"type_code":-1,"tag":-1,"keyword":-1,"key":-1,"lat":"0","lng":"0","center_name":-1,"has_package":-1,"has_special":0,"has_conference":1,"order":-1,"dur":-1,"bud":-1,"page":1,"num":"","cap_num":"","qt":0}'
    # }
    datas = {'email': '2670617835@qq.com', 'password': 'g2670617835', 'remember': True}

    url = "https://www.yunpanjingling.com/user/login"
    # session = requests.session()
    requ = requests.post(url, data=urlencode(datas), headers=headers)
    res = requ.text
    print(res)

ajaxRequest()