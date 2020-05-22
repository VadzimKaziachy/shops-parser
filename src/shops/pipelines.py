# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import os
import requests
from typing import List, NoReturn

from .items import TwentyFirstCenturyItem
from .settings import BACKEND_URL


class TwentyFirstCenterPipeline(object):

    def __init__(self) -> NoReturn:
        self.products: List[TwentyFirstCenturyItem] = list()

    def process_item(self, product, spider) -> TwentyFirstCenturyItem:
        self.products.append(product)
        return product

    def close_spider(self, spider) -> NoReturn:
        requests.patch(
            url=BACKEND_URL.format(backend_host=os.environ['BACKEND_HOST'], job_id=os.environ['SCRAPY_JOB']),
            json={'data': [dict(item) for item in self.products]}
        )
