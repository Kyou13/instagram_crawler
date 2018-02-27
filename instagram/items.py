# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# 特定のハッシュタグの投稿の情報
class userItem(scrapy.Item):
    userId = scrapy.Field()
    postNum = scrapy.Field()
    followerNum = scrapy.Field()
    followingNum = scrapy.Field()
    url = scrapy.Field()

class goodItem(scrapy.Item):
    userId = scrapy.Field()
    postId = scrapy.Field()
    postURL = scrapy.Field()
    goodNum = scrapy.Field()


class InstagramItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class MapionspiderItem(scrapy.Item):
    name = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    pass
