from flask_combo_jsonapi import ResourceDetail, ResourceList
from blog.schemas import TagSchema
from blog.models import db
from blog.models import TagModel


class TagList(ResourceList):
    schema = TagSchema
    data_layer = {
        "session": db.session,
        "model": TagModel,
    }
class TagDetail(ResourceDetail):
    schema = TagSchema
    data_layer = {
        "session": db.session,
        "model": TagModel,
    }
