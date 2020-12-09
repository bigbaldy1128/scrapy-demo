# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CsdnItem(scrapy.Item):
    type = scrapy.Field()
    name = scrapy.Field()
    desc = scrapy.Field()

