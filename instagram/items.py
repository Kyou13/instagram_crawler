# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# 特定のハッシュタグの投稿の情報
class HashItem(scrapy.Item):
    '''
    ・投稿者
    ・いいねをした人
    ・投稿画像（画像のURLでもいいかな）
    '''
    userId = scrapy.Field()
    # good_userId = scrapy.Field()


class InstagramItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
