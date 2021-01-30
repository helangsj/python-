# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhanzhangsucaiItem(scrapy.Item):
    # define the fields for your item here like:
    image_name = scrapy.Field()
    imgage_url = scrapy.Field()

