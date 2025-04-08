import re

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from articles.spiders.wiki import WikiSpider


class LastUpdatedPipeline:
    def process_item(self, item, spider):
        if 'last_updated' in item:
            item['last_updated'] = item['last_updated'].replace(
                'This page was last edited on ', ''
            )
            item['last_updated'] = item['last_updated'].replace(', at', '')
            item['last_updated'] = item['last_updated'].strip('. ')

        return item


class TextPipeline:
    def process_item(self, item, spider):
        item = ItemAdapter(item)
        item['text'] = [p.get_text() for p in item.get('text', [])]
        item['text'] = '\n'.join(item.get('text', []))
        item['text'] = re.sub(r'\[[0-9]+\]', '', item.get('text', ''))

        return item
