# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv
import os
from itemadapter import ItemAdapter


class AnimePipeline:
    def open_spider(self, spider):
        os.makedirs('output', exist_ok=True)
        self.file = open('output/anime_data.csv', 'w', newline='', encoding='utf-8')
        self.writer = csv.writer(self.file)
        self.writer.writerow([
            "Native",
            "Romaji",
            "English",
            "Type",
            "Status",
            "Studios",
            "Start date",
            "Genre(s)",
            "Rate",
            "Total",
            "Summary Description"
        ])

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        self.writer.writerow([
            adapter.get('Native'),
            adapter.get('Romaji'),
            adapter.get('English'),
            adapter.get('Type'),
            adapter.get('Status'),
            adapter.get('Studios'),
            adapter.get('Start_date'),
            adapter.get('Genres'),
            adapter.get('Rate'),
            adapter.get('Total'),
            adapter.get('Summary_description')
        ])
        return item
