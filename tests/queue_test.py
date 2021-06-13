import unittest

from core.queue import Queue

class TestSetup(unittest.TestCase):
    def test_should_create_connections(self):
       queue = Queue(queue_name=None)
       queue.setup()

       self.assertTrue(queue.connection)
       self.assertTrue(queue.channel)

if __name__ == '__main__':
    unittest.main()