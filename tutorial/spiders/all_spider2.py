# @author wangjinzhao on 2020/12/9
import scrapy
from scrapy.utils.response import open_in_browser

from tutorial.items import Item


class AllSpider2(scrapy.Spider):
    name = "all-2"
    allowed_domains = ["toscrape.com"]
    start_urls = [
        "http://quotes.toscrape.com/"
    ]

    def parse(self, response):
        for sel in response.xpath('//div[@class="quote"]'):
            self.logger.info('parse 1')
            item = {
                'text': sel.xpath('span[@class="text"]/text()').get(),
                'tags': sel.css('div.tags a.tag::text').getall()
            }

            yield from response.follow_all(urls=sel.css('.author + a'), callback=self.parse_author, cb_kwargs=dict(item=item))

        # yield from response.follow_all(css='ul.pager a', callback=self.parse)

    def parse_author(self, response, item):
        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        item['author'] = {
            'name': extract_with_css('h3.author-title::text'),
            'birthdate': extract_with_css('.author-born-date::text')
        }
        yield item
