# -*- coding: utf-8 -*-

import argparse
import logging
from app import init_app


def setup_logger(level=None):
    """
    Setup logger with given loglevel. If no loglevel is provided, use DEBUG
    as default fallback.

    :param level: loglevel used for logger
    :type level: int
    """
    if level is None:
        level = logging.DEBUG

    logging.basicConfig(level=level)


def main(hostname: str, port: int, loglevel=None):
    """
    Run Flask using integrated webserver
    """
    setup_logger(level=loglevel)
    app = init_app()
    app.run(host=hostname, port=port)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Tutron, the python robot')
    parser.add_argument('--hostname', type=str, default="0.0.0.0",
                        required=False, help='hostname to use for the app')
    parser.add_argument('--port', type=int, default=5050, required=False,
                        help='port which the app should listen on')
    parser.add_argument('--loglevel', type=int, default=None, required=False,
                        help='set loglevel to certain value')
    args = parser.parse_args()

    main(hostname=args.hostname, port=args.port)
