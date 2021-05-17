from scrapy import Spider

class Andraste(Spider):
    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(Andraste, cls).from_crawler(crawler, *args, **kwargs)
        signals.spider_closed = handle_spider_closed()
        return spider

    

