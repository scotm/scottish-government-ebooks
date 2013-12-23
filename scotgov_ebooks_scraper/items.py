# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class ScotgovEbooksScraperItem(Item):
    # define the fields for your item here like:
    # name = Field()
    title = Field()
    author = Field()
    pub_date = Field()
    url = Field()
    epub_link = Field()
    mobi_link = Field()
