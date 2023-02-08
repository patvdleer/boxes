import unittest
from dataclasses import dataclass


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


class TestCompoundProduct(unittest.TestCase):
    def test_compound_product(self):
        from boxes.presets.shapes import Cylinder
        from boxes.presets.products.product import CompoundProduct

        weird_bottle = CompoundProduct(name="Revell small sample", components={
            "bottle lid": Cylinder(diameter=33, height=3.2),
            "bottle": Cylinder(diameter=23, height=12),
        })

        assert weird_bottle.width == 33
        assert weird_bottle.height == 12

    def test_compound_product_extended(self):
        from boxes.presets.shapes import Cylinder
        from boxes.presets.products.product import CompoundProduct

        @dataclass
        class WeirdBottle(CompoundProduct):
            categories = [
                "test"
            ]

        weird_bottle = WeirdBottle(name="Revell small sample", components={
            "bottle lid": Cylinder(diameter=33, height=3.2),
            "bottle": Cylinder(diameter=23, height=12),
        })

        assert weird_bottle.width == 33
        assert weird_bottle.height == 12
