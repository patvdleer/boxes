import json
from typing import List, Dict, Tuple, Union, Type

from boxes.presets.shapes import Shape


class PresetConfig:
    """ I should really review this code """
    mapping: dict

    def __init__(self, mappings: Dict[Type[Shape], List[Union[Tuple, Dict]]]):
        self.mapping = {}
        for k, v in mappings.items():
            self.add(k, v)

    def add(self, klass: type[Shape], mapping: List[Union[Tuple, Dict]]):
        self.mapping[klass] = mapping

    def to_json(self):
        return json.dumps(self.categorised())

    def categorised(self):
        from boxes.presets import PRESETS
        data = {
            "Uncategorised": {}
        }

        for shape_klass, shape_mapping in self.mapping.items():
            for klass_name, inst in PRESETS.items():
                if not isinstance(inst, shape_klass):
                    continue

                klass_data = {}
                for shape_prop, model_prop in shape_mapping:
                    klass_data[model_prop] = getattr(inst, shape_prop)

                if hasattr(inst, "categories") and len(inst.categories) > 0:
                    for category in inst.categories:
                        if category not in data.keys():
                            data[category] = {}
                        data[category][klass_name] = klass_data
                    continue

                data["Uncategorised"][klass_name] = klass_data

        return data

    def flat(self):
        from boxes.presets import PRESETS
        data = {}
        for shape_klass, shape_mapping in self.mapping.items():
            for klass_name, inst in PRESETS.items():
                if not isinstance(inst, shape_klass):
                    continue

                data[klass_name] = {}
                for shape_prop, model_prop in shape_mapping:
                    data[klass_name][model_prop] = getattr(inst, shape_prop)

        return data


