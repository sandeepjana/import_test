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
    msg = "from .bg.bg_src import fun"
    from .bg.bg_src import fun
    fun(msg)
except ImportError as e:
    warn(e, msg)