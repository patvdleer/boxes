import unittest
from dataclasses import dataclass


class TestRegistry(unittest.TestCase):
    def test_registry_presets(self):
        from boxes.presets import PRESETS
        assert len(PRESETS) > 0


class TestPresetConfig(unittest.TestCase):
    def test_apply(self):
        from boxes.generators.can_storage import CanStorage
        can_storage = CanStorage()
        can_storage.presets.flat()

    def test_json(self):
        from boxes.generators.can_storage import CanStorage
        can_storage = CanStorage()
        can_storage.presets.categorised()


class TestProduct(unittest.TestCase):
    def test_product_categories(self):
        from boxes.presets.shapes import Cylinder
        from boxes.presets import Product

        @dataclass
        class TestProductWOCat(Product, Cylinder):
            pass

        @dataclass
        class TestProductWCat(Product, Cylinder):
            categories = [
                "Battery"
            ]

        prod_wo_cat = TestProductWOCat(name="07540", diameter=7.5, height=40)
        assert isinstance(prod_wo_cat.categories, list)

        prod_w_cat = TestProductWCat(name="07540", diameter=7.5, height=40)
        assert isinstance(prod_w_cat.categories, list)
        assert "Battery" in prod_w_cat.categories
