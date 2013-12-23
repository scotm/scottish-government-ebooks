# Scrapy settings for scotgov_ebooks_scraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'scotgov_ebooks_scraper'

SPIDER_MODULES = ['scotgov_ebooks_scraper.spiders']
NEWSPIDER_MODULE = 'scotgov_ebooks_scraper.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'scotgov_ebooks_scraper (+http://www.example.com)'
HTTPCACHE_ENABLED = True