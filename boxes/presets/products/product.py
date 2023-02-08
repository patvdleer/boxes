from dataclasses import dataclass, field
from typing import List, Dict

from boxes.presets.shapes import Shape, Circle, Cylinder


@dataclass
class Product:
    name: str
    categories: List[str] = field(init=False)

    def __post_init__(self):
        """ due to kw_only being PY3.10+ """
        if not hasattr(self, "categories") or not self.categories:
            self.categories = []


@dataclass
class CompoundProduct(Product):
    components: Dict[str, Shape]

    @property
    def width(self) -> float:
        _max = 0
        for comp in self.components.values():
            if isinstance(comp, (Circle, Cylinder)):
                if comp.diameter > _max:
                    _max = comp.diameter
            # elif isinstance(comp, (Rectangle, Cuboid)):
            elif hasattr(comp, "width"):
                if comp.width > _max:
                    _max = comp.width
        if _max == 0:
            raise AttributeError
        return _max

    @property
    def height(self) -> float:
        _max = 0
        for comp in self.components.values():
            # if isinstance(comp, (Cylinder, Cuboid)):
            if hasattr(comp, "height"):
                if comp.height > _max:
                    _max = comp.height
        if _max == 0:
            raise AttributeError
        return _max

    @property
    def diameter(self) -> float:
        _max = 0
        for comp in self.components.values():
            if hasattr(comp, "diameter"):
                if comp.diameter > _max:
                    _max = comp.diameter
        if _max == 0:
            raise AttributeError
        return _max

    @property
    def radius(self) -> float:
        return self.diameter / 2
