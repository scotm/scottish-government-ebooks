# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class ScotgovEbooksScraperItem(Item):
    # define the fields for your item here like:
    # name = Field()
    Title = Field()
    Author = Field()
    Publication_Date = Field()
    URL = Field()
    ePub_link = Field()
    MOBI_link = Field()
