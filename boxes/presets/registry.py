from __future__ import annotations

from typing import List, Union, Dict

from boxes.presets.products.product import Product


class Registry:
    _instance = None

    presets: Dict[str, Product] = {}

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

    def register(self, cls: Union[Product, List[Product]]):
        if isinstance(cls, list):
            for p in cls:
                self.register(p)
            return
        self.presets[cls.name] = cls


def register(cls: Union[Product, List[Product]]):
    Registry().register(cls)
