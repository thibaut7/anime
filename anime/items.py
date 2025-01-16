# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AnimeItem(scrapy.Item):
    Native = scrapy.Field()
    Romaji = scrapy.Field()
    English = scrapy.Field()
    Type = scrapy.Field()
    Status = scrapy.Field()
    Studios = scrapy.Field()
    Start_date = scrapy.Field()
    Genres = scrapy.Field()
    Rate = scrapy.Field()
    Total = scrapy.Field()
    Summary_description = scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
