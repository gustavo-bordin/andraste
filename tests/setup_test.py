from argparse import ArgumentParser
import unittest

from andraste import Setup


VALID_ARGS = [
    "mfc"
]

class FakeCrawler:
    pass

class TestSetup(unittest.TestCase):
    def test_should_create_args(self):
        setup = Setup()
        setup._create_parser()
        setup._create_args()
        setup.args = setup.args.parse_args(['bot.bot.MySpider'])

        for arg in VALID_ARGS:
            self.assertIn(arg, vars(setup.args))

    def test_should_get_crawler_reference(self):
        setup = Setup()
        setup._create_parser()
        setup._create_args()
        setup.args = setup.args.parse_args(['tests.setup_test.FakeCrawler'])
        setup._get_crawler_reference()
        self.assertEqual(setup.crawler_class, FakeCrawler)
        
if __name__ == '__main__':
    unittest.main()