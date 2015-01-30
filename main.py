__author__ = 'Alex Gusev <alex@flancer64.com>'
import sys
import logging
from prxgt.app import App
from prxgt.config import Config

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s]: %(message)s')


def main(argv):
    # read configuration file
    cfg = Config()
    # create application main class and run it
    app = App(cfg)
    app.run()
    return 0


def entry_point():
    """Zero-argument entry point for use with setuptools/distribute."""
    raise SystemExit(main(sys.argv))


if __name__ == '__main__':
    entry_point()