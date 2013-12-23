scottish-government-ebooks
==========================

A scrapy project for obtaining Scottish Government ebooks.

# Requirements

[Python 2.6 or 2.7](http://www.python.org/)
[Scrapy](http://scrapy.org/)

# Instructions

1. Clone the repository, cd into the repository, then cd into 'it_ebooks'.

2. To get a copy of the it-books database in CSV format, issue the following command.

   1. scrapy crawl it_ebooks -t csv -o output.csv

Patches welcome.
