from flask_combo_jsonapi import ResourceDetail, ResourceList
from blog.schemas import AuthorSchema
from blog.models.database import db
from blog.models import AuthorModel

class AuthorList(ResourceList):
    schema = AuthorSchema
    data_layer = {
    "session": db.session,
    "model": AuthorModel,
    }
class AuthorDetail(ResourceDetail):
    schema = AuthorSchema
    data_layer = {
    "session": db.session,
    "model": AuthorModel,
    }