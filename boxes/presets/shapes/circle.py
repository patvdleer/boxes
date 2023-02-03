import math
from dataclasses import dataclass


@dataclass
class Circle:
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
