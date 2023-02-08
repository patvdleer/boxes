from dataclasses import dataclass

from boxes.presets.products.basics import Bottle, BottleSquare
from boxes.presets.products.product import CompoundProduct
from boxes.presets.registry import register
from boxes.presets.shapes import Cylinder

_categories = [
    "Paint",
    "Model making",
]


@dataclass
class PaintBottle(Bottle):
    categories = _categories


@dataclass
class PaintBottleSquare(BottleSquare):
    categories = _categories


register([
    PaintBottle(name="Model Master 15ml", diameter=33, height=48),
    PaintBottle(name="Vallejo model wash", diameter=35.5, height=74.5),
    PaintBottle(name="Tamiya color acrylic paint", diameter=40.5, height=50),
    CompoundProduct(name="Revell small sample", components={
        "bottle lid": Cylinder(diameter=33, height=3.2),
        "bottle": Cylinder(diameter=23, height=12),
    }),
    PaintBottleSquare(name="Revell Aqua Colour", width=33, length=34.5, height=42),
])
