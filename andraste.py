import argparse
import importlib

from scrapy.crawler import CrawlerProcess


def _create_args(parser):
    parser.add_argument("mfc", help="Provide module.file.ClassName")
    return parser


def _run(class_reference):
    process = CrawlerProcess({})
    process.crawl(class_reference)
    process.start()


def _get_class_reference(args):
    module, file, class_name = args.mfc.split('.')
    file_reference = importlib.import_module(f'{module}.{file}')
    class_reference = getattr(file_reference, class_name)
    return class_reference


def _create_parser():
    parser = argparse.ArgumentParser(description="Runs a crawler class")
    return parser
    

def main():
    parser = _create_parser()
    args = _create_args(parser)
    args.parse_args()
    class_reference = _get_class_reference(args)
    _run(class_reference)


if __name__ == "__main__":
    main()