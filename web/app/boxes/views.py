from flask import render_template, abort

from .blueprint import boxes_app
from .utils import get_box_model


@boxes_app.route('/', methods=['GET'])
def homepage():
    return render_template('list.html')


@boxes_app.route('/list', methods=['GET'])
def list():
    return render_template('list.html')


@boxes_app.route('/<group_name>', methods=['GET'])
def view_group(group_name: str):
    return render_template('list.html')


@boxes_app.route('/<group_name>/<box_name>', methods=['GET'])
def view_box(group_name: str, box_name: str):
    box = get_box_model(box_name, group_name)
    if box is None:
        abort(404)
    return render_template(
        'view.html',
        group_name=group_name,
        box_name=box_name,
        box=box
    )
