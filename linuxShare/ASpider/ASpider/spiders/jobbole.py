# -*- coding: utf-8 -*-
# import datetime
# import sys
# import re
from urllib import parse

import scrapy
from scrapy.http import Request
# from scrapy.loader import ItemLoader

from ASpider.items import JobBoleArticleItem, ArticleItemLoader
from ASpider.utils.common import get_md5


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):

        # 1.获取文章列表中的文章url，并交给scrapy下载后并进行解析
        # 2.获取下一页的url并交给scrapy进行下载，下载完成后交给parse

        # 解析列表页中的所有文章url，并交给scrapy下载后并进行解析\
        # post_urls = response.css("#archive .floated-thumb .post-thumb a::attr(href)").extract()
        post_nodes = response.css("#archive .floated-thumb .post-thumb a")
        for post_node in post_nodes:
            image_url = post_node.css("img::attr(src)").extract_first("")
            post_url = post_node.css("::attr(href)").extract_first("")
            #将Request交给scrapy ，yield会自动交给scrapy下载
            #通过meta（字典）将image_url 通过Request（异步调用）传递给parse_detail中的response
            #parse.urljoin()如果post_url没有域名，则从response.url取域名，如果有则不受影响
            yield Request(url=parse.urljoin(response.url, post_url),
                          meta={"front_image_url": image_url},
                          callback=self.parse_detail)
            print(post_url)
            ##提取下一页，并交给scripy下载
            next_url = response.css(".next.page-numbers::attr(href)").extract_first("")
            if next_url:
                yield Request(url=parse.urljoin(response.url, next_url),
                              callback=self.parse)


    def parse_detail(self, response):
        # 提取文章的具体字段
        article_item = JobBoleArticleItem()
        # ##通过css选择器提取字段
        # # front_image_url = response.meta["front_image_url"]
        # front_image_url = response.meta.get("front_image_url", "")  # 文章封面图
        # title = response.css(".entry-header h1::text").extract()
        # create_date = response.css("p.entry-meta-hide-on-mobile::text").extract()[0].strip().replace("·",
        #                                                                                              "").strip()  # p元素可以直接选择text
        # # 获取span标签中class为vote-post-up获取h10标签的内容
        # # praise_nums = response.css("span.vote-post-up h10::text").extract()[0]
        # # 获取class为vote-post-up获取h10标签的内容
        # praise_nums = response.css(".vote-post-up h10::text").extract()[0]
        # fav_nums = response.css(".bookmark-btn::text").extract()[0]
        # match_re = re.match(".*?(\d+).*", fav_nums)
        # if match_re:
        #     fav_nums = int(match_re.group(1))
        # else:
        #     fav_nums = 0
        #
        # #获取a标签中属性为href为#article-comment下span标签的的内容
        # comment_nums = response.css("a[href='#article-comment'] span::text").extract()[0]
        # match_re = re.match(".*?(\d+).*", comment_nums)
        # if match_re:
        #     comment_nums = int(match_re.group(1))
        # else:
        #     comment_nums = 0
        #
        # content = response.css("div.entry").extract_first("")
        # #获取p标签中class为entry-meta-hide-on-mobile中a标签的内容
        # tags = response.css("p.entry-meta-hide-on-mobile a::text").extract()
        # tag_list = [element for element in tags if not element.strip().endswith("评论")]
        #
        # tags = ",".join(tag_list)
        #
        # articleItem["url_object_id"] = get_md5(response.url)
        # articleItem["title"] = title
        # articleItem["url"] = response.url
        # try:
        #     create_date = datetime.datetime.struct_time(create_date, "%Y/%m/%d").date()
        # except Exception as e:
        #     create_date = datetime.datetime.now()
        # articleItem["create_date"] = create_date
        # articleItem["front_image_url"] = [front_image_url]
        # articleItem["praise_nums"] = praise_nums
        # articleItem["comment_nums"] = comment_nums
        # articleItem["fav_nums"] = fav_nums
        # articleItem["tags"] = tags
        # articleItem["content"] = content

        # 通过itemloader 加载item
        front_image_url = response.meta.get("front_image_url", "")  # 文章封面图s
        item_loader = ArticleItemLoader(item=JobBoleArticleItem(),response=response)
        item_loader.add_css("title", ".entry-header h1::text")
        # item_loader.add_css("title", ".entry-header h1::text")
        item_loader.add_value("url", response.url)
        item_loader.add_value("url_object_id", get_md5(response.url))
        item_loader.add_css("create_date", "p.entry-meta-hide-on-mobile::text")
        item_loader.add_value("front_image_url", [front_image_url])
        item_loader.add_css("praise_nums", ".vote-post-up h10::text")
        item_loader.add_css("comment_nums", "a[href='#article-comment'] span::text")
        item_loader.add_css("fav_nums", ".bookmark-btn::text")
        item_loader.add_css("tags", "p.entry-meta-hide-on-mobile a::text")
        item_loader.add_css("content", "div.entry")

        article_item = item_loader.load_item()

        yield article_item
