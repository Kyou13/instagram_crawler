import re
import json
import pandas as pd

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http.request import Request

from instagram.items import userItem
from scrapy_splash import SplashRequest

class HashSpider(CrawlSpider):
    name = "getUserData"
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
            yield SplashRequest(url, self.parse_item, args={'wait': 0.5},)

    def parse_item(self, response):
        self.account = response.url.split('/')[-2]
        followerNum = response.css('span._fd86t ::text').extract()[1]
        followerNum = followerNum.replace('k','')
        followerNum = int( float(followerNum)*1000 )
        # ユーザーデータの取得
        item = userItem(
            userId = self.account,
            postNum = response.css('span._fd86t ::text').extract()[0],
            followerNum = followerNum,
            followingNum = response.css('span._fd86t ::text').extract()[2],
            url = response.url,
            )
        yield item
