from dataclasses import dataclass

from boxes.presets.products.basics import Bottle, BottleSquare


@dataclass
class GlueBottle(Bottle):
    categories = [
        "Glue",
    ]


@dataclass
class GlueBottleSquare(BottleSquare):
    categories = [
        "Glue",
    ]
