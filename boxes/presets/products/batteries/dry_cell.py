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
    DryCellCylindrical(name="AA", height=50.5, diameter=14.5),
    DryCellCylindrical(name="AAA", height=44.5, diameter=10.5),
    DryCellCylindrical(name="AAAA", height=42.5, diameter=8.3),
    DryCellCylindrical(name="B", height=60, diameter=21.5),
    DryCellCylindrical(name="C", height=50, diameter=26.2),
    DryCellCylindrical(name="D", height=61.5, diameter=34.2),
    DryCellCylindrical(name="N", height=30.2, diameter=12),
    DryCellCylindrical(name="A23", height=28.5, diameter=10.3),
    DryCellCylindrical(name="A27", height=28.2, diameter=8),
])
