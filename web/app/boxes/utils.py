from typing import Dict

from boxes import generators
from boxes.generators import ui_groups_by_name, UIGroup
from boxes.generators.traylayout import TrayLayout2

__group_box_models = None


def get_group_box_models() -> Dict[str, UIGroup]:
    global __group_box_models
    if not __group_box_models:
        _boxes = {b.__name__: b for b in generators.getAllBoxGenerators().values() if b.webinterface}
        _boxes['TrayLayout2'] = TrayLayout2
        groups_by_name = ui_groups_by_name
        for name, box in _boxes.items():
            groups_by_name.get(box.ui_group, groups_by_name["Misc"]).add(box)
        __group_box_models = groups_by_name
    return __group_box_models


def get_group_uimodel(group_name) -> UIGroup:
    for group in get_group_box_models().values():
        if group.name == group_name:
            return group


def get_box_model(name: str, group_name: str = None):
    for group in get_group_box_models().values():
        if group_name:
            if group.name != group_name:
                continue

        for box in group.generators:
            if box.__name__ == name:
                return box
