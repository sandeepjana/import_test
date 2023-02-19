# __main__.py will be executed when the package itself is invoked directly
# from the command line using the -m flag.
# https://docs.python.org/3/library/__main__.html#main-py-in-python-packages
from pkg import try_import
import sys


def main(msg):
    try_import.try_import(msg)


if __name__ == "__main__":
    main(" ".join(sys.argv[1:]))
