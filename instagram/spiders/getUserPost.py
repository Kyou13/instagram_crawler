# -*- coding: utf-8 -*-
import json
import pandas as pd

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http.request import Request

from instagram.items import goodItem
from scrapy_splash import SplashRequest

class HashSpider(CrawlSpider):
    name = "getUserPost"
    allowed_domains = ["instagram.com"]

    # 引数でタグを指定
    def __init__(self):
        # ここで複数アカウントを指定
        df = pd.read_csv('./data/participant_data.csv')
        accounts = df[df['アカウント名']!='メールにて聞いてるなう']['アカウント名'].dropna()
        accounts = accounts.tolist()
        self.start_urls = ['http://www.instagram.com/{}/'.format(a) for a in accounts]

    def start_requests(self):
        for url in self.start_urls:
            self.stepNextPageNum = 0
            yield SplashRequest(url, self.parse_item, args={'wait': 0.5},)

    def parse_item(self, response):
        self.account = response.url.split('/')[-2]
        #We get the json containing the photos's path
        js = response.selector.xpath('//script[contains(., "window._sharedData")]/text()').extract()
        js = js[0].replace('window._sharedData = ', '') # 純粋なJSONデータのみ取り出す。
        jscleaned = js[:-1]
        #Load it as a json object
        locations = json.loads(jscleaned)
        #We check if there is a next page
        user = locations['entry_data']['ProfilePage'][0]['user']
        has_next = user['media']['page_info']['has_next_page']
        media = user['media']['nodes']

        img_urls = response.css('div._mck9w._gvoze._tn0ps a::attr(href)').extract()
        for url in img_urls:
            yield SplashRequest(response.urljoin(url), self.parse_goodNum, args={'wait': 0.5})

        maxPageNum = 10
        # If there is a next page, we crawl it
        if self.stepNextPageNum<maxPageNum & has_next:
            url = response.url+"/?max_id="+media[-1]['id']
            yield SplashRequest(url, callback=self.parse_item, args={'wait': 0.5},)
        self.stepNextPageNum += 1 #  10ページ以上取得しないためのフラグ。

    def parse_goodNum(self, response):
        goodNum = response.css('div._3gwk6._nt9ow span::text').extract_first()
        item = goodItem(
            userId = response.url.split('=')[-1],
            postId = response.url.split('/')[4],
            postURL = response.url.rsplit('/', 1)[0], # できたら、パラメータを捨てたい。
            goodNum = response.css('div._3gwk6._nt9ow span::text').extract_first(),
        )
        yield item
