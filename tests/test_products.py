import unittest


class TestProduct(unittest.TestCase):

    def test_registry(self):
        from boxes.presets import PRESETS
        assert len(PRESETS) > 0
