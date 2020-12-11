# @author wangjinzhao on 2020/12/9
import scrapy

from tutorial.items import Item


class QuotesSpider(scrapy.Spider):
    name = "quote"
    allowed_domains = ["toscrape.com"]
    start_urls = [
        "http://quotes.toscrape.com/"
    ]

    def parse(self, response):
        for sel in response.xpath('//div[@class="quote"]'):
            yield {
                'text': sel.xpath('span[@class="text"]/text()').get(),
                'author': sel.css('small.author::text').get(),
                'tags': sel.css('div.tags a.tag::text').getall()
            }
        yield from response.follow_all(css='ul.pager a', callback=self.parse)
