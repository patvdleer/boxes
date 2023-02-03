from .products import *

PRESETS = {}


def get_presets():
    from .registry import Registry
    global PRESETS
    PRESETS = Registry().presets

get_presets()
