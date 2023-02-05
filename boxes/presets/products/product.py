from dataclasses import dataclass, field
from typing import List


@dataclass
class Product:
    name: str
    categories: List[str] = field(init=False)

    def __post_init__(self):
        """ due to kw_only being PY3.10+ """
        if not hasattr(self, "categories") or not self.categories:
            self.categories = []

