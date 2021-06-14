import json
import time

from scrapy.crawler import CrawlerProcess
from crochet import setup

from core.queue import Queue
from helpers.flow_helpers import get_queue_name


class Flow:
    def __init__(self, crawler_class):
        setup()
        self.crawler_class = crawler_class

    def _on_receive_input(self, *args):
        input_received = args[3]
        print(f'Received: {input_received}')

        json_input = json.loads(input_received)

        runner = CrawlerProcess()
        runner.crawl(self.crawler_class, input_=json_input)
        time.sleep(1)
        print('Input processed, getting next input...')

    def start(self):
        queue_name = get_queue_name(
            class_name=self.crawler_class.__name__,
            queue_type="inputs"
        )
        queue = Queue(queue_name)
        queue.setup()
        
        queue.consume(callback=self._on_receive_input)
        queue.channel.start_consuming()

        
