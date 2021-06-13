import pika


class Queue:
    def __init__(self, queue_name):
        self.channel = None
        self.connection = None
        self.queue_name = queue_name
        self.inputs = []
        
    def _create_connection(self):
        connection = pika.BlockingConnection()

        self.connection = connection

    def _create_channel(self):
        channel = self.connection.channel()

        self.channel = channel

    def _define_queue(self):
        self.channel.queue_declare(queue=self.queue_name)

    def setup(self):
        self._create_connection()
        self._create_channel()

    def close_connection(self):
        self.connection.close()
       
    def consume(self, callback):
        self.channel.basic_consume(
            self.queue_name, 
            callback, 
            auto_ack=True
        )
        





    