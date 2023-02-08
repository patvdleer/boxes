from dataclasses import dataclass

from boxes.presets.products.product import Product
from boxes.presets.shapes.cuboid import Cuboid
from boxes.presets.shapes.cylinder import Cylinder


@dataclass
class Bottle(Product, Cylinder):
    pass


@dataclass
class BottleSquare(Product, Cuboid):
    pass

