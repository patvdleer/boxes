from .blueprint import boxes_app
from .utils import get_group_box_models


@boxes_app.context_processor
def inject_group_box_models():
    return {
        "group_box_models": get_group_box_models()
    }
