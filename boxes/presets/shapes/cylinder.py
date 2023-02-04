import math
from dataclasses import dataclass

from .circle import Circle


@dataclass
class Cylinder(Circle):
    _n_dimensions = 3
    height: float

    @property
    def volume(self) -> float:
        return math.pi * (self.radius**2) * self.height
