from dataclasses import dataclass

from boxes.presets.products.product import Product
from boxes.presets.registry import register
from boxes.presets.shapes.cuboid import Cuboid


@dataclass
class PlayingCard(Product, Cuboid):
    pass


register([
    PlayingCard(name="Mini American", width=41, length=63, height=0.025),
    PlayingCard(name="Mini European", width=44, length=68, height=0.025),
    PlayingCard(name="Standard American", width=57, length=89, height=0.025),
    PlayingCard(name="Standard European", width=59, length=92, height=0.025),
    PlayingCard(name="Standard Card Game", width=63.5, length=88, height=0.025),
    PlayingCard(name="Tarrot", width=70, length=120, height=0.025),
])
