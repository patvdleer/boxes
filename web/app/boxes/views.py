import mimetypes
import os
import sys
import tempfile
import traceback
from typing import List, Dict

from flask import render_template, abort, Response, request, send_file

from boxes import Boxes
from .blueprint import boxes_app
from .exceptions import ArgumentParserError
from .utils import get_box_class, get_group_ui_model, get_box_form_filled


@boxes_app.route('/', methods=['GET'])
def homepage():
    return render_template('list.html')


@boxes_app.route('/<group_name>', methods=['GET'])
def view_group(group_name: str):
    group = get_group_ui_model(group_name)
    if group is None:
        abort(404)
    return render_template('view_group.html', group_name=group_name, group=group)


@boxes_app.route('/<group_name>/<box_name>', methods=['GET'])
def view_box(group_name: str, box_name: str):
    box_cls = get_box_class(box_name, group_name)
    if box_cls is None:
        abort(404)
    box = box_cls()
    box.form = get_box_form_filled(box, request.args)
    render = request.args.get("render", "0")
    if render in ["1", "2"]:
        return render_box(box, request.args, render == "2")
    return render_template(
        'view_box.html',
        group_name=group_name,
        box_name=box_name,
        box=box
    )


def render_box(box: Boxes, args: Dict[str, str], as_attachment=False) -> Response:
    args = [f"--{key}={value}" for key, value in args.items() if not key.startswith("render")]
    try:
        box.parseArgs(args)
    except ArgumentParserError as e:
        return abort(500, e)

    extension = box.format
    if extension == "svg_Ponoko":
        extension = "svg"

    try:
        fd, box.output = tempfile.mkstemp()
        box.metadata["url"] = request.url
        box.open()
        box.render()
        box.close()
    except Exception as e:
        if not isinstance(e, ValueError):
            print("Exception during rendering:", file=sys.stderr)
            traceback.print_exc()
        return abort(500, e)
    response = send_file(
        box.output,
        download_name=f"{box.__class__.__name__}.{extension}",
        as_attachment=as_attachment
    )
    os.close(fd)
    os.remove(box.output)
    return response
