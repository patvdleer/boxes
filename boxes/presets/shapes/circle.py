import math
from dataclasses import dataclass

from .shape import Shape


@dataclass
class Circle(Shape):
    _n_dimensions = 2
    diameter: float

    @property
    def radius(self) -> float:
        return self.diameter / 2

    @radius.setter
    def set_radius(self, radius) -> None:
        self.diameter = radius * 2

    @property
    def circumference(self) -> float:
        return math.pi * self.diameter
