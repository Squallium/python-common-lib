import logging

import fire
from pyfiglet import Figlet
from rich.console import Console
from rich.logging import RichHandler


class PythonCommonLib:

    def __init__(self) -> None:
        super().__init__()


class MainDefaultTest:

    @staticmethod
    def test():
        print('Hi, test')


console = Console(force_terminal=True, width=150)
FORMAT = "%(message)s"
logging.basicConfig(
    level=logging.INFO,
    format=FORMAT,
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True, tracebacks_show_locals=True, console=console)]
)

log = logging.getLogger("rich")
log.info(Figlet().renderText("Python Common Lib"))

if __name__ == '__main__':
    fire.Fire(PythonCommonLib)