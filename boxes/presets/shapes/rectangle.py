from dataclasses import dataclass

from .shape import Shape


@dataclass
class Rectangle(Shape):
    _n_dimensions = 2
    width: float
    length: float
