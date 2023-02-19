# import sys
# import pathlib
# FILE = pathlib.Path(__file__).resolve()
# ROOT_DIR = str(FILE.parents[2])
# sys.path.append(ROOT_DIR)
# # ^ inserts project root to sys.path
# # so that pkg.bg.src1 makes sense
# print(ROOT_DIR)
from rich import print


def warn(e, msg):
    print(f':cross_mark: [yellow]{e}: [bold]{msg}[/][/]')


try:
    msg = "from pkg.bg.bg_src import fun"
    from pkg.bg.bg_src import fun
    fun(msg)
except ImportError as e:
   warn(e, msg)

try:
    msg = "from ..bg.bg_src import fun"
    from ..bg.bg_src import fun
    fun(msg)
except ImportError as e:
    warn(e, msg)
