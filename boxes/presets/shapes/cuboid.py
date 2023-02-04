from dataclasses import dataclass

from .rectangle import Rectangle


@dataclass
class Cuboid(Rectangle):
    height: float
