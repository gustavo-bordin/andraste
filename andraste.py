import argparse
import importlib


class Setup:
    def __init__(self):
        self.parser = None
        self.args = None
        self.crawler_class = None

    def _create_args(self):
        self.parser.add_argument("mfc", help="Provide module.file.ClassName")
        self.args = self.parser

    def _get_crawler_reference(self):
        path_to_class = self.args.mfc.split('.')
        path_to_file = '.'.join(path_to_class[:-1])
        class_name = path_to_class[-1]

        file_reference = importlib.import_module(path_to_file)
        self.crawler_class = getattr(file_reference, class_name)

    def _create_parser(self):
        parser = argparse.ArgumentParser(description="Runs a crawler class")
        self.parser = parser
    
    def start(self):
        self._create_parser()
        self._create_args()
        self.args = self.args.parse_args()
        self._get_crawler_reference()

if __name__ == "__main__":
    setup = Setup()
    setup.start()