# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PrisMysqlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ReactorItem(scrapy.Item):
    Country = scrapy.Field()
    ENTC = scrapy.Field()
    ReactorNo = scrapy.Field()