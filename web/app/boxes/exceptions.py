import argparse
import boxes


class ArgumentParserError(Exception):
    pass


class ThrowingArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        raise ArgumentParserError(message)


# Evil hack
boxes.ArgumentParser = ThrowingArgumentParser  # type: ignore
