import unittest

from andraste import _create_parser
from andraste import _create_args


VALID_ARGS = [
    "mfc"
]


class TestArgs(unittest.TestCase):
    def test_should_create_args(self):
        parser = _create_parser()
        parser_with_args = _create_args(parser)
        parsed_args = parser_with_args.parse_args(['bot.bot.MySpider'])

        for arg in VALID_ARGS:
            self.assertIn(arg, vars(parsed_args))
        
if __name__ == '__main__':
    unittest.main()