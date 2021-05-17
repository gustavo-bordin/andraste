import unittest
import sys

sys.path.append("..")
from andraste import _create_parser
from andraste import _create_args


VALID_ARGS = [
    "mfc"
]


class TestArgs(unittest.TestCase):
    def test_should_create_args(self):
        parser = _create_parser()
        args = _create_args(parser)
        
        for arg in VALID_ARGS:
            self.assertIn(arg, vars(args))
        
if __name__ == '__main__':
    unittest.main()