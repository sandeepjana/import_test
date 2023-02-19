from rich import print


def warn(e, msg):
    print(f":cross_mark: [yellow]{e}: [bold]{msg}[/][/]")


def try_import(msg=''):
    success = True
    try:
        way = "from pkg.bg.bg_src import fun: "
        from pkg.bg.bg_src import fun

        fun(way + msg)
    except ImportError as e:
        warn(e, msg)
        success = False

    try:
        way = "from .bg.bg_src import fun: "
        from .bg.bg_src import fun

        fun(way + msg)
    except ImportError as e:
        warn(e, msg)
        success = False

    return success


if __name__ == "__main__":
    try_import('Hello')
