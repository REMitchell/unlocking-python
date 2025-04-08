import scrapy
from bs4 import BeautifulSoup
from articles.items import ArticleItem


class WikiSpider(scrapy.Spider):
    custom_settings = {'ITEM_PIPELINES': {'articles.pipelines.TextPipeline': 200}}

    name = 'wiki'
    allowed_domains = ['wikipedia.org']
    start_urls = [
        'https://en.wikipedia.org/wiki/Python_(programming_language)',
        'https://en.wikipedia.org/wiki/Monty_Python',
        'https://en.wikipedia.org/wiki/Pythonidae',
    ]

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        article = ArticleItem()
        article['url'] = response.url
        article['title'] = soup.select_one('h1#firstHeading').get_text()
        article['last_updated'] = soup.select_one('li#footer-info-lastmod').get_text()
        # article['text'] = soup.select('div.mw-content-ltr p')

        '''
        last_updated = soup.select_one('li#footer-info-lastmod').get_text()
        last_updated = last_updated.replace('This page was last edited on ', '')
        last_updated = last_updated.replace(', at', '')
        article['last_updated'] = last_updated.strip('. ')
        
        paras = soup.select('div.mw-content-ltr p')
        article['text'] = '\n'.join([p.get_text() for p in paras])[0:100]
        '''
        return article
