# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ChinaSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    province = scrapy.Field()
    province_code = scrapy.Field()
    city = scrapy.Field()
    city_code = scrapy.Field()
    county = scrapy.Field()
    county_code = scrapy.Field()
    township = scrapy.Field()
    township_code = scrapy.Field()
    neighborhood_committee = scrapy.Field()
    neighborhood_committee_code = scrapy.Field()
