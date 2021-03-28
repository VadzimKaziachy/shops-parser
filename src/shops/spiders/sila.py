import re
from typing import Optional

from scrapy import Spider
from scrapy.http import XmlRpcRequest
from scrapy_selenium import SeleniumRequest

from shops.items import ProductItem


class SilaSpider(Spider):
    name = "sile_spider"
    allowed_domains = ['www.sila.by']
    start_urls = []

    def __init__(self, category: Optional[str] = None, *args, **kwargs):
        self.start_urls.append(category)
        super().__init__(*args, **kwargs)

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(url=url, callback=self.parse_pages, cb_kwargs={"url": url})

    def parse_pages(self, response, **kwargs):
        max_page = max(map(int, response.css("div.pages a::attr(href)").re(r".+[page/](\d+)")), default=1)
        for page in range(1, max_page):
            yield XmlRpcRequest(url=f"{kwargs['url']}/page/{page}", callback=self.parse)

    def parse(self, response, **kwargs):
        for product in response.css("div.tov_prew"):
            yield ProductItem(
                name=product.css("strong::text").get(),
                code=re.search(r"[\(\.+ ](\d+)[\)]", product.css("sup::text").get()).group(1),
                price=float(product.css("div.price b::text").get()) * 1000,
            )
