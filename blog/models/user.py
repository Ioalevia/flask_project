from sqlalchemy import Column, Integer, String, Boolean
from blog.models import db
from flask_login import UserMixin


class UserModel(db.Model, UserMixin):
    id = Column(Integer, primary_key=True)
    username = Column(String(80), nullable=False)
    first_name = Column(String(80))
    last_name = Column(String(80))
    email = Column(String(255), unique=True, nullable=False,)
    is_staff = Column(Boolean, nullable=False, default=False)


def __repr__(self):
    return f"<User #{self.id} {self.username!r}>"
