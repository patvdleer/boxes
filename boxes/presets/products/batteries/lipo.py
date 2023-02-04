from dataclasses import dataclass

from boxes.presets.products.product import Product
from boxes.presets.registry import register
from boxes.presets.shapes.cylinder import Cylinder


@dataclass
class LiPo(Product, Cylinder):
    """ LiPo battery

    source: https://en.wikipedia.org/wiki/List_of_battery_sizes#Lithium-ion_batteries_(rechargeable)
    """
    categories = [
        "Battery"
    ]


register([
    LiPo(name="07540", height=7.5, diameter=40),
    LiPo(name="08570", height=8.5, diameter=70),
    LiPo(name="10180", height=10., diameter=18),
    LiPo(name="10280", height=10., diameter=28),
    LiPo(name="10440", height=10., diameter=45),
    LiPo(name="10850", height=10., diameter=85),
    LiPo(name="13400", height=13., diameter=40),
    LiPo(name="14250", height=14., diameter=25),
    LiPo(name="14300", height=14., diameter=30),
    LiPo(name="14500", height=14., diameter=53),
    LiPo(name="14650", height=14., diameter=65),
    LiPo(name="15270", height=15., diameter=27),
    LiPo(name="16340", height=16., diameter=34),
    LiPo(name="16650", height=16., diameter=65),
    LiPo(name="17500", height=17., diameter=50),
    LiPo(name="17650", height=17., diameter=65),
    LiPo(name="17670", height=17., diameter=67),
    LiPo(name="18350", height=18., diameter=35),
    LiPo(name="18490", height=18., diameter=49),
    LiPo(name="18500", height=18., diameter=50),
    LiPo(name="18650", height=18., diameter=65),
    LiPo(name="20700", height=20., diameter=70),
    LiPo(name="21700", height=21., diameter=70),
    LiPo(name="25500", height=25., diameter=50),
    LiPo(name="26500", height=26., diameter=50),
    LiPo(name="26650", height=26., diameter=65),
    LiPo(name="26800", height=26., diameter=80),
    LiPo(name="32600", height=32., diameter=60),
    LiPo(name="32650", height=32., diameter=67.7),
    LiPo(name="38120", height=38., diameter=120),
    LiPo(name="38140", height=38., diameter=140),
    LiPo(name="40152", height=40., diameter=152),
    LiPo(name="4680", height=46., diameter=80),
])
