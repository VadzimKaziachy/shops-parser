# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import pika
import json

from shops import settings
from shops.items import TwentyFirstCenturyItem


class ProductsPipeline(object):

    def __init__(self) -> None:
        parameters = pika.URLParameters(settings.RABBITMQ_URL)

        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()

    def process_item(self, product, spider) -> TwentyFirstCenturyItem:
        self.channel.basic_publish(
            exchange="",
            routing_key=settings.RABBITMQ_QUEUE,
            body=json.dumps(dict(product)).encode(),
        )
        return product

    def close_spider(self, spider) -> None:
        self.connection.close()
