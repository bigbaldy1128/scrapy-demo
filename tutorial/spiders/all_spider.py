# @author wangjinzhao on 2020/12/9
import scrapy

from tutorial.author import Author
from tutorial.items import Item
import logging
import threading


class AllSpider(scrapy.Spider):
    name = "all-1"
    allowed_domains = ["toscrape.com"]
    start_urls = [
        "http://quotes.toscrape.com/"
    ]

    def parse(self, response):
        for sel in response.xpath('//div[@class="quote"]'):
            item = Item()
            item['text'] = sel.xpath('span[@class="text"]/text()').get()
            item['tags'] = sel.css('div.tags a.tag::text').getall()
            response.follow_all(urls=sel.css('.author + a'), callback=self.parse_author, cb_kwargs=dict(item=item))

        # yield from response.follow_all(css='ul.pager a', callback=self.parse)

    def parse_author(self, response, item):
        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        author = Author()
        author['name'] = extract_with_css('h3.author-title::text')
        author['birthdate'] = extract_with_css('.author-born-date::text')

        item['author'] = author
        yield item
