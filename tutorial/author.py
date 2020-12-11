# @author wangjinzhao on 2020/12/10
import scrapy


class Author(scrapy.Item):
    name = scrapy.Field()
    birthdate = scrapy.Field()