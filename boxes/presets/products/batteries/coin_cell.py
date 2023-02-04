from dataclasses import dataclass

from boxes.presets.products.product import Product
from boxes.presets.registry import register
from boxes.presets.shapes.cylinder import Cylinder


@dataclass
class CoinCell(Product, Cylinder):
    """ Coin cell battery

    Name is in IEC

    source: https://en.wikipedia.org/wiki/List_of_battery_sizes#Button_cells_%E2%80%93_coin,_watch
    """
    ansi: str = None
    categories = [
        "Battery"
    ]


register([
    CoinCell(name="CR927", diameter=9.5, height=2.7),
    CoinCell(name="CR1025", ansi="5033LC", diameter=10, height=2.5),
    CoinCell(name="CR1130", diameter=11.5, height=3),
    CoinCell(name="CR1216", ansi="5034LC", diameter=12.5, height=1.6),
    CoinCell(name="CR1220", ansi="5012LC", diameter=12.5, height=2.0),
    CoinCell(name="CR1225", ansi="5020LC", diameter=12.5, height=2.5),
    CoinCell(name="CR1616", diameter=16, height=1.6),
    CoinCell(name="CR1620", ansi="5009LC", diameter=16, height=2),
    CoinCell(name="CR1632", diameter=16, height=3.2),
    CoinCell(name="CR2012", diameter=20, height=1.2),
    CoinCell(name="CR2016", ansi="5000LC", diameter=20, height=1.6),
    CoinCell(name="CR2020", diameter=20, height=2),
    CoinCell(name="CR2025", ansi="5003LC", diameter=20, height=2.5),
    CoinCell(name="CR2032", ansi="5004LC", diameter=20, height=3.2),
])
