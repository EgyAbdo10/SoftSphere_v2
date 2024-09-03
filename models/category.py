#!/usr/bin/python3
"""create the Category model"""

from models.base_model import BaseModel, Base, storage_type
from sqlalchemy import Column, String

class Category(BaseModel, Base):
    """create Categories instances"""
    if storage_type == "db":
        __tablename__ = "categories"
        name = Column("name", String(60), nullable=False)
    else:
        name = ""
    def __init__(self, **kwargs):
        """
        instansiate a Category instance
        and gives it a name
        """
        super().__init__()
        for key, val in kwargs.items():
            setattr(self, key, val)
