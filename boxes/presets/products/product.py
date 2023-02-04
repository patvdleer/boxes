from dataclasses import dataclass, field
from typing import List


@dataclass
class Product:
    name: str
    categories: List[str] = field(default_factory=lambda: [])
