# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join


# 自定义Item Loader
class WPItemLoader(ItemLoader):
    default_input_processor = TakeFirst()


# 自定义Item
class WPSearchItem(scrapy.Item):
    title = scrapy.Field()


class WpsourcewebsiteItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
