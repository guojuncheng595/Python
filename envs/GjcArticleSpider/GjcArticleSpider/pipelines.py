# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exporters import JsonItemExporter
from twisted.enterprise import adbapi
import codecs  # 文件的打开
import json
import MySQLdb
import MySQLdb.cursors


class GjcarticlespiderPipeline(object):
    def process_item(self, item, spider):
        return item


# 图片处理Pipeline
class ArticleImagePipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        for ok, value in results:
            image_file_path = value["path"]
        item["front_image_path"] = image_file_path
        return item

# 链接数据库操作 -- 拆用同步的机制写入MySQL数据库
class MysqlPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect('127.0.0.1', 'root', 'root', 'scrapyspider', charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        insert_sql = """
            insert into jobbole_article(title, url, create_date, fav_nums)
            values (%s, %s, %s, %s)
        """
        self.cursor.execute(insert_sql, (item["title"], item["url"], item["create_date"], item["fav_nums"]))
        self.conn.commit()

#数据库链接, 使用adbapi.ConnectionPool 实现异步操作数据
class MysqlTwistedPipline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbparms = dict(
            host=settings["MYSQL_HOST"],
            db=settings["MYSQL_DBNAME"],
            user=settings["MYSQL_USER"],
            password=settings["MYSQL_PASSWORD"],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        # 将sql编程异步操作
        dbpool = adbapi.ConnectionPool("MySQLdb", **dbparms)
        return cls(dbpool)

    def process_item(self, item, spider):
        # 使用twisted将MySQL插入变成异步执行
        query = self.dbpool.runInteraction(self.do_insert, item)
        query.addErrback(self.handle_error) # 处理异常

    def handle_error(self, failure):
        # 处理异步插入的异常
        print(failure)

    def do_insert(self, cursor, item):
        # 执行具体的插入
        insert_sql = """
                    insert into jobbole_article(title, url, create_date, fav_nums)
                    values (%s, %s, %s, %s)
                """
        cursor.execute(insert_sql, (item["title"], item["url"], item["create_date"], item["fav_nums"]))


# 保存json的pipline
class JsonWithEncodingPipeline(object):
    def __init__(self):
        self.file = codecs.open('article.json', 'w', encoding="utf-8")

    # 打开文件
    def process_item(self, item, spider):
        lines = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(lines)
        return item

    # 关闭文件
    def spider_closed(self, spider):
        self.file.close()


class JsonExporterPipleline(object):
    # 调用scrapy提供的json export导出json文件
    # 自定义json文件的导出
    def __init__(self):
        self.file = open('articleexport.json', 'wb')
        self.export = JsonItemExporter(self.file, encoding="utf-8", ensure_ascii=False)
        self.export.start_exporting()

    def close_spider(self,spider):
        self.export.finish_exporting()  # 停止导出
        self.file.close()

    def process_item(self, item, spider):
        self.export.export_item(item)
        return item
