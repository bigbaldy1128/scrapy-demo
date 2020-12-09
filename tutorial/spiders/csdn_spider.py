# @author wangjinzhao on 2020/12/9
import scrapy

from tutorial.items import CsdnItem


class CsdnSpider(scrapy.Spider):
    name = "test"
    allowed_domains = ["toscrape.com"]
    start_urls = [
        "http://quotes.toscrape.com/page/1/"
    ]

    def parse(self, response):
        for sel in response.xpath('//div[@class="quote"]'):
            yield {
                'text': sel.xpath('span[@class="text"]/text()').get(),
                'author': sel.css('small.author::text').get(),
                'tags': sel.css('div.tags a.tag::text').getall()
            }
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)