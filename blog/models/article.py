from sqlalchemy import Column, Integer, ForeignKey, String, Text, DateTime, func
from sqlalchemy.orm import relationship
from blog.models import db
from datetime import datetime


class ArticleModel(db.Model):
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey("author_model.id"))
    author = relationship("AuthorModel", back_populates="articles")
    title = Column(String(200), nullable=False, default="", server_default="")
    body = Column(Text, nullable=False, default="", server_default="")
    dt_created = Column(DateTime, default=datetime.utcnow, server_default=func.now())
    dt_updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)