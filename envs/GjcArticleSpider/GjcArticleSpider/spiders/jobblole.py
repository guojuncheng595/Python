# -*- coding: utf-8 -*-
import re
from urllib import parse

import scrapy
import datetime
from scrapy.http import Request

from GjcArticleSpider.items import JobBoleArticleItem
from GjcArticleSpider.utils.common import get_md5

class JobbloleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts']

    def parse(self, response):

        # 获取下一页的url并交给srapy进行下载
        # 1.获取文章列表页中的文章url并交给scrapy下载后并进行解析
        # 2.获取下一页的url并交给srapy进行下载
        # 3.下载完成后交给parse函数
        post_nodes = response.css("#archive .floated-thumb .post-thumb a")

        for post_node in post_nodes:
            #获取url
            image_url = post_node.css("img::attr(src)").extract_first("")
            post_url = post_node.css("::attr(href)").extract_first("")
            # http拼接url
            yield Request(url=parse.urljoin(response.url, post_url), meta={"front_image_url": image_url}, callback=self.parse_detail)

        # 提取下一页，并交给scrapy下载
        next_url = response.css(".next.page-numbers::attr(href)").extract_first()
        if next_url:
            yield Request(url=parse.urljoin(response.url, post_url), callback=self.parse)

    def parse_detail(self, response):
        article_item = JobBoleArticleItem()

        ###################################xpath实现内容爬取字段###########################################################
        # re_selector = response.xpath("/html/body/div[1]/div[3]/div[1]/div[1]/h1")
        # re2_selector = response.xpath('//*[@id="post-110287"]/div[1]/h1/text()')
        # re3_selector = response.xpath('//div[@class="entry-header"]/h1/text()')
        #
        # create_date = response.xpath("//p[@class='entry-meta-hide-on-mobile']/text()").extract_first().strip().replace(
        #     "·", "").strip()
        # praise_nums = response.xpath("//span[contains(@class,'vote-post-up')]/h10/text()").extract()[0]
        # fav_nums = response.xpath("//span[contains(@class,'bookmark-btn')]/text()").extract()[0]
        # match_re = re.match(".*(\d+).*", fav_nums)
        # if match_re:
        #     fav_nums = int(match_re.group(1))
        # else:
        #     fav_nums = 0
        #
        # comment_nums = response.xpath("//a[@href='#article-comment']/span").extract()[0]
        # match_re = re.match(".*(\d+).*", comment_nums)
        # if match_re:
        #     comment_nums = int(match_re.group(1))
        # else:
        #     comment_nums = 0
        #
        # content = response.xpath("//div[@class='entry']").extract()[0]
        # tag_list = response.xpath("//p[@class='entry-meta-hide-on-mobile']/a/text()").extract()
        # tag_list = [element for element in tag_list if not element.strip().endswith("评论")]
        # tags = ",".join(tag_list)

        ####################################css实现内容爬取字段#############################################################
        title = response.css(".entry-header h1::text").extract()[0]
        create_date = response.css("p.entry-meta-hide-on-mobile::text").extract()[0].strip().replace("·", "").strip()
        praise_nums = response.css(".vote-post-up h10::text").extract()[0]
        front_image_url = response.meta.get("front_image_url", "") # 文章封面图
        fav_nums = response.css(".bookmark-btn::text").extract()[0]
        match_re = re.match(".*(\d+).*", fav_nums)
        if match_re:
            fav_nums = int(match_re.group(1))
        else:
            fav_nums = 0

        comment_nums = response.css("a[href='#article-comment'] span::text").extract()[0]
        match_re = re.match(".*(\d+).*", comment_nums)
        if match_re:
            comment_nums = int(match_re.group(1))
        else:
            comment_nums = 0

        content = response.css("div.entry").extract()[0]

        tag_list = response.css("p.entry-meta-hide-on-mobile a::text").extract()
        tag_list = [element for element in tag_list if not element.strip().endswith("评论")]
        tags = ",".join(tag_list)

        article_item["url_object_id"] = get_md5(response.url)
        article_item["title"] = title
        article_item["url"] = response.url
        try:
            create_date = datetime.datetime.strptime(create_date,"%Y/%m/%d").date()
        except Exception as e:
            create_date = datetime.datetime.now().date()
        article_item["create_date"] = create_date
        article_item["front_image_url"] = [front_image_url]
        article_item["praise_nums"] = praise_nums
        article_item["comment_nums"] = comment_nums
        article_item["fav_nums"] = fav_nums
        article_item["tags"] = tags
        article_item["content"] = content

        yield article_item  # 该行执行后，到items.py文件


        pass
