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
    LiPo(name="07540", diameter=7.5, height=40),
    LiPo(name="08570", diameter=8.5, height=70),
    LiPo(name="10180", diameter=10., height=18),
    LiPo(name="10280", diameter=10., height=28),
    LiPo(name="10440", diameter=10., height=45),
    LiPo(name="10850", diameter=10., height=85),
    LiPo(name="13400", diameter=13., height=40),
    LiPo(name="14250", diameter=14., height=25),
    LiPo(name="14300", diameter=14., height=30),
    LiPo(name="14500", diameter=14., height=53),
    LiPo(name="14650", diameter=14., height=65),
    LiPo(name="15270", diameter=15., height=27),
    LiPo(name="16340", diameter=16., height=34),
    LiPo(name="16650", diameter=16., height=65),
    LiPo(name="17500", diameter=17., height=50),
    LiPo(name="17650", diameter=17., height=65),
    LiPo(name="17670", diameter=17., height=67),
    LiPo(name="18350", diameter=18., height=35),
    LiPo(name="18490", diameter=18., height=49),
    LiPo(name="18500", diameter=18., height=50),
    LiPo(name="18650", diameter=18., height=65),
    LiPo(name="20700", diameter=20., height=70),
    LiPo(name="21700", diameter=21., height=70),
    LiPo(name="25500", diameter=25., height=50),
    LiPo(name="26500", diameter=26., height=50),
    LiPo(name="26650", diameter=26., height=65),
    LiPo(name="26800", diameter=26., height=80),
    LiPo(name="32600", diameter=32., height=60),
    LiPo(name="32650", diameter=32., height=67.7),
    LiPo(name="38120", diameter=38., height=120),
    LiPo(name="38140", diameter=38., height=140),
    LiPo(name="40152", diameter=40., height=152),
    LiPo(name="4680", diameter=46., height=80),
])
