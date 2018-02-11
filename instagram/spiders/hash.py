# -*- coding: utf-8 -*-
import scrapy
# from scrapy.spiders import CrawlSpider, Rule
# from scrapy.linkextractors import LinkExtractor
#
# from scrapy.spider import BaseSpider
# from scrapy.selector import HtmlXPathSelector
# from scrapy.http.request import Request

from instagram.items import HashItem


class HashSpider(scrapy.Spider):
    name = "hash"
    allowed_domains = ["instagram.com"]
    tag = 'kawaii'
    start_urls = ['https://www.instagram.com/explore/tags/{}/?hl=ja'.format(tag)]

    # rules = (
    #     Rule(LinkExtractor(allow=r'/tokyo/rstLst/lunch/\d/')),
    #     Rule(LinkExtractor(allow=r'/tokyo/A\d+/A\d+/\d+/$'), callback='parse_restaurant'),
    # )

    def parse(self, response):
        pass
