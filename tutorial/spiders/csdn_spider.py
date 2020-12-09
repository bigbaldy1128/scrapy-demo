# @author wangjinzhao on 2020/12/9
import scrapy

from tutorial.items import CsdnItem


class CsdnSpider(scrapy.Spider):
    name = "csdn"
    allowed_domains = ["csdn.net"]
    start_urls = [
        "http://bbs.csdn.net/"
    ]

    def parse(self, response):
        for sel in response.xpath('//label[@class="recom_t"]'):
            item = CsdnItem()
            item['type'] = sel.xpath('a[@class="classify"]/text()').extract()
            item['name'] = sel.xpath('a[@class="recom_who"]/text()').extract()
            item['desc'] = sel.xpath('a[@class="recom_title"]/text()').extract()
            yield item