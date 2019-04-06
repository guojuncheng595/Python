
from scrapy.cmdline import execute

import sys
import os

# os.path.dirname()   #所在的父目录
# os.path.abspath(__file__)   #文件目录
# D:\Desktop\python-learning\envs\GjcArticleSpider
# D:\Desktop\python-learning\envs\GjcArticleSpider\main.py
# print(os.path.dirname(os.path.abspath(__file__)))
# print(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl", "jobbole"])
