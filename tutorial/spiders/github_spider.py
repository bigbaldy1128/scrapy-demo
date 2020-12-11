# @author wangjinzhao on 2020/12/9
import scrapy
from scrapy import FormRequest

from tutorial.items import Item


class GithubSpider(scrapy.Spider):
    name = "github"
    allowed_domains = ["https://github.com/"]
    login_url = 'https://github.com/login'
    start_urls = [
        "https://github.com/"
    ]

    def login(self , response):
        data = {
            'name' : 'USERNAME',
            'pass' : 'PASSWORD',
            'login' : 'login'
        }
        yield FormRequest(url=self.login_url, formdata=data ,callback=self.parse)

    def parse(self, response):
        for sel in response.xpath('//div[@class="quote"]'):
            yield {
                'text': sel.xpath('span[@class="text"]/text()').get(),
                'author': sel.css('small.author::text').get(),
                'tags': sel.css('div.tags a.tag::text').getall()
            }
        yield from response.follow_all(css='ul.pager a', callback=self.parse)
