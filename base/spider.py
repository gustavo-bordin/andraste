from datetime import datetime
from core.queue import Queue

from helpers.flow_helpers import get_queue_name

from scrapy import Spider
from scrapy import signals


class Andraste(Spider):
    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(Andraste, cls).from_crawler(crawler, *args, **kwargs)
        cls._setup_signals(crawler, spider)
        cls._setup_output_queue(spider)
        return spider

    @classmethod
    def _setup_signals(cls, crawler, spider):
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        crawler.signals.connect(spider.item_scraped, signal=signals.item_scraped)

    @classmethod
    def _setup_output_queue(cls, spider):
        queue_name = get_queue_name(
            class_name=spider.__class__.__name__, 
            queue_type="outputs"
        )

        print('\n\n\n\n\nqueue name\n\n\n\n\n' + str(queue_name))
        cls.queue = Queue(queue_name)
        cls.queue.setup()   
        
    def spider_closed(cls):
        cls.queue.close_connection()

    def item_scraped(cls, item, spider):
        metadata = cls._create_metadata(spider)
        item['metadata'] = metadata
        
        is_fields_ok = cls._validate_fields(item, spider)

        if not is_fields_ok:
            print(f"The field didnt pass the validations: {item}")
            return

        cls.queue.publish(message=item)


    def _create_metadata(cls, spider):
        now = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
        return {'input': spider.input_, 'processingDate': now}

    def _validate_fields(cls, item, spider):
        def validate_builtins():
            return item.get('data') and item.get('metadata')

        def validate_requireds():
            for required_field in spider.required_fields:
                if item['data'].get(required_field) is None:
                    return False
            
            return True

        return validate_builtins() and validate_requireds()

