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

        runner = CrawlerProcess()
        runner.crawl(self.crawler_class, input=input_received)

        print('Input processed, getting next input...')

    def start(self):
        queue_name = get_queue_name(self.crawler_class)
        queue = Queue(queue_name)
        queue.setup()
        
        queue.consume(callback=self._on_receive_input)
        queue.channel.start_consuming()

        
