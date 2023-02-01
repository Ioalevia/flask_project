from flask_combo_jsonapi import ResourceDetail, ResourceList
from blog.schemas import UserSchema
from blog.models.database import db
from blog.models import UserModel

class UserList(ResourceList):
    schema = UserSchema
    data_layer = {
    "session": db.session,
    "model": UserModel,
    }
class UserDetail(ResourceDetail):
    schema = UserSchema
    data_layer = {
    "session": db.session,
    "model": UserModel,
    }