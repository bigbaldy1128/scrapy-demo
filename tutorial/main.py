# @author wangjinzhao on 2020/12/10
from scrapy.crawler import CrawlerProcess

from tutorial.spiders.all_spider2 import AllSpider2

process = CrawlerProcess()
process.crawl(AllSpider2)