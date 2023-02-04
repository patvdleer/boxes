from dataclasses import dataclass

from .rectangle import Rectangle


@dataclass
class Cuboid(Rectangle):
    _n_dimensions = 3
    height: float
