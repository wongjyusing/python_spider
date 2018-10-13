# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup as bs
from scrapy.http import Request
class ChinaSpider(scrapy.Spider):
    name = 'china'
    #allowed_domains = ['www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/index.html']
    allowed_domains = ['www.stats.gov.cn']
    start_urls = ['http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/index.html']

    def parse(self, response):
        items = {}
        soup = bs(response.text,'lxml')
        for item in soup.select('.provincetr a'):
            city_url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/' + item['href']
            items['province'] = item.text
            yield Request(url=city_url,meta=items,callback=self.parse_chapter)

    def parse_chapter(self,response):
        soup = bs(response.text,'lxml')
        for item in soup.select('.citytr a'):
            print(item.text)
# {级别：广东省}
