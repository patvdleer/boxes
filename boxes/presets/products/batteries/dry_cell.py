from dataclasses import dataclass

from boxes.presets.products.product import Product
from boxes.presets.registry import register
from boxes.presets.shapes.cylinder import Cylinder


@dataclass
class DryCellCylindrical(Product, Cylinder):
    """ DryCell cylindrical battery

    source: https://en.wikipedia.org/wiki/List_of_battery_sizes#Cylindrical_batteries
    """
    categories = [
        "Battery"
    ]


register([
    DryCellCylindrical(name="AA", diameter=50.5, height=14.5),
    DryCellCylindrical(name="AAA", diameter=44.5, height=10.5),
    DryCellCylindrical(name="AAAA", diameter=42.5, height=8.3),
    DryCellCylindrical(name="B", diameter=60, height=21.5),
    DryCellCylindrical(name="C", diameter=50, height=26.2),
    DryCellCylindrical(name="D", diameter=61.5, height=34.2),
    DryCellCylindrical(name="N", diameter=30.2, height=12),
    DryCellCylindrical(name="A23", diameter=28.5, height=10.3),
    DryCellCylindrical(name="A27", diameter=28.2, height=8),
])
