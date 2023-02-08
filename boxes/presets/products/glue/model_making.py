from .abstract import GlueBottle, GlueBottleSquare
from boxes.presets.registry import register

_categories = [
    "Glue",
    "Model making"
]

register([
    GlueBottle(name="Microscale Industries MI-1 Micro Set", diameter=30, height=71.5),
    GlueBottle(name="Microscale Industries MI-2 Micro Sol", diameter=30, height=71.5),
    GlueBottleSquare(name="Tamiya cement", width=42.5, length=42.5, height=64),
])
