# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup as bs
from scrapy.http import Request
class NovelSpider(scrapy.Spider):
    name = 'novel'
    allowed_domains = ['gulongwang.com']
    start_urls = ['https://gulongwang.com/']

    def parse(self, response):
        base_url = 'https://gulongwang.com'
        items = {}
        soup = bs(response.text,'lxml')
        for item in soup.select('p a'):
            items['book_link'] = base_url + item['href']
            items['book_name'] = item.text

            yield Request(url=items['book_link'],meta=items,callback=self.parse_chapter)


    def parse_chapter(self,response):
        #print(response.text)
        print(response.meta)
