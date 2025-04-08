from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from bs4 import BeautifulSoup
from articles.items import ArticleItem
from articles.spiders.wiki import WikiSpider


class WikicrawlerSpider(CrawlSpider):
    name = 'wikicrawler'
    allowed_domains = ['wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Benevolent_dictator_for_life']

    rules = (
        Rule(LinkExtractor(allow='(wiki/)((?!:).)*$'), callback='parse', follow=True),
    )

    parse = WikiSpider.parse
