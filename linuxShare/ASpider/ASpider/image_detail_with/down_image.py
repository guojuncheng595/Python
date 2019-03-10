#-*-coding:utf-8-*-
import requests

def spider():
    url = "https://www.epailive.com/basic/captcha?ran=0.22070346581876787"
    for i in range(1, 101):
        print("正在下载的张数是：",i)
        with open("D:\Desktop\python-learning\linuxShare\ASpider\ASpider\image_detail_with\image\{}.png".format(i), "wb") as f:
            f.write(requests.get(url).content)
spider()