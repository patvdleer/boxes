import unittest


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
