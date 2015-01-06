__author__ = 'scott'

from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scotgov_ebooks_scraper.items import ScotgovEbooksScraperItem
from dateutil import parser

class BooksListSpider(CrawlSpider):
    name = 'books_list'
    allowed_domains = ['scotgov.publishingthefuture.info']
    start_urls = ['http://scotgov.publishingthefuture.info/e-books']

    rules = (
        Rule(SgmlLinkExtractor(allow=r'/publication/'), callback='parse_item', follow=True),
        Rule(SgmlLinkExtractor(allow=r'/e-books'), follow=True),
    )

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        i = ScotgovEbooksScraperItem()
        #i['domain_id'] = hxs.select('//input[@id="sid"]/@value').extract()
        i['Title'] = hxs.select("//h1/text()").extract()[0].strip()
        i['Author'] = hxs.select('//div[contains(@class,"field-name-field-author")]/div[@class="field-items"]/div/a/text()').extract()[0].strip()
        i['URL'] = response.url.strip()
        pub_date = hxs.select('//div[contains(@class,"field-name-field-publication-date")]/div[@class="field-items"]/div/span/text()').extract()[0]
        try:
            pub_date = parser.parse(pub_date)
        except:
            pass
        i['Publication_Date'] = pub_date
        epub = hxs.select('//a[contains(@href,".epub")]/@href').extract()
        i['ePub_link'] = epub[0] if epub else ''
        mobi = hxs.select('//a[contains(@href,".mobi")]/@href').extract()
        i['MOBI_link'] = mobi[0] if mobi else ''
        return i
