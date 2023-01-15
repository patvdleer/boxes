import argparse
import os

from app import create_app, config


class EnvDefault(argparse.Action):
    def __init__(self, envvar, required=True, default=None, **kwargs):
        if not default and envvar:
            if envvar in os.environ:
                default = os.environ[envvar]
        if required and default:
            required = False
        super().__init__(default=default, required=required, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, values)


parser = argparse.ArgumentParser(
    prog="boxes.py",
)
parser.add_argument(
    "--host",
    action=EnvDefault,
    envvar="HOST",
    help="IP to bind to",
    required=True,
    type=str,
    default='0.0.0.0',
    dest="host",
)
parser.add_argument(
    "-p",
    "--port",
    action=EnvDefault,
    envvar="PORT",
    help="Port to run webservice for on",
    required=True,
    type=int,
    default=9091,
    dest="port",
)
parser.add_argument(
    "--debug",
    action="store_true",
    help="Debug mode",
    default=False,
    dest="debug",
)

# parser.add_argument("-V", "--version", action="version", version=f"%(prog)s {__version__}")


def main(host: str, port: int, debug=False, **kwargs):
    _config = config.dev_config
    for k, v in kwargs.items():
        _config.__setattr__(_config, k.upper(), v)
    app = create_app(_config)
    app.run(host=host, port=port, debug=debug)


if __name__ == "__main__":
    main(**vars(parser.parse_args()))
