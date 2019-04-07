    # -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import re
import scrapy
import datetime
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join


class GjcarticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


def add_jobbole(value):
    return value+"-jobbole1"


def date_convert(value):
    try:
        create_date = datetime.datetime.strftime(value, "%Y/%m/%d").date()
    except Exception as e:
        create_date = datetime.datetime.now().date()
    return create_date


class ArticleItemLoader(ItemLoader):
    # 自定义Itemloader
    default_output_processor = TakeFirst()


def return_value(value):
    return value


def get_num(value):
    match_re = re.match(".*(\d+).*", value)
    if match_re:
        nums = int(match_re.group(1))
    else:
        nums = 0
    return nums


def remove_comment_tag(value):
    # 去掉tag中提取的评论
    if '评论' in value:
        return ""
    else:
        return value


# 自定义Item
class JobBoleArticleItem(scrapy.Item):
    title = scrapy.Field()
    create_date = scrapy.Field(
        input_processor=MapCompose(date_convert),
    )
    url = scrapy.Field()
    url_object_id = scrapy.Field()
    front_image_url = scrapy.Field(
        output_processor=MapCompose(return_value)
    )
    front_image_path = scrapy.Field()
    praise_nums = scrapy.Field(
        input_processor=MapCompose(get_num)
    )
    comment_nums = scrapy.Field(
        input_processor=MapCompose(get_num)
    )
    fav_nums = scrapy.Field(
        input_processor=MapCompose(get_num)
    )
    tags = scrapy.Field(
        input_processor=MapCompose(remove_comment_tag),
        output_processor=Join(",")
    )
    content = scrapy.Field()