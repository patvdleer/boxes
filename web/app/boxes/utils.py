import argparse
from typing import Dict, List

import markdown
from flask_babel import gettext

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


def get_group_ui_model(group_name: str) -> UIGroup:
    for group in get_group_box_models().values():
        if group.name == group_name:
            return group


def get_box_model(name: str, group_name: str = None):
    box_cls = get_box_class(name, group_name)
    if box_cls:
        return box_cls()


def get_box_class(name: str, group_name: str = None):
    for group in get_group_box_models().values():
        if group_name:
            if group.name != group_name:
                continue

        for box in group.generators:
            if box.__name__ == name:
                return box


def get_box_form(box) -> List[Dict]:
    group_actions = []
    # not sure why this is wanted
    # for group in box.argparser._action_groups:
    for group_ in box.argparser._action_groups[3:] + box.argparser._action_groups[:3]:
        if not group_._group_actions:
            continue
        if len(group_._group_actions) == 1 and isinstance(group_._group_actions[0], argparse._HelpAction):
            continue

        prefix = getattr(group_, "prefix", None)
        group_data = {
            "title": group_.title,
            "prefix": prefix,
            "actions": []
        }

        for action in group_._group_actions:
            if isinstance(action, argparse._HelpAction):
                continue
            if action.dest in ("input", "output"):
                continue

            name = action.option_strings[0].replace("-", "")
            action_data = {
                "name": name,
                "viewname": name,
                "input_value": None,
                "input_type": "input",
                "input_html": None,
                "help": action.help,
                "default": action.default,
                "choices": action.choices,
                "required": action.required,
            }

            if action.help:
                action_data['help'] = markdown.markdown(action.help)

            if isinstance(action, argparse._StoreAction) and hasattr(action.type, "html"):
                action_data['input_type'] = "custom"
                action_data['input_html'] = action.type.html(name, action.default, gettext)
            elif action.dest == "Layout":
                action_data['input_type'] = "textarea"
            elif action.choices:
                action_data['input_type'] = "select"

            if prefix and name.startswith(prefix + '_'):
                action_data['viewname'] = name[len(prefix) + 1:]

            group_data['actions'].append(action_data)
        group_actions.append(group_data)
    return group_actions


def get_box_form_filled(box, values: dict) -> List[Dict]:
    box_form = get_box_form(box)
    for group in box_form:
        for action in group['actions']:
            action['value'] = values.get(action['name'], None)
    return box_form
