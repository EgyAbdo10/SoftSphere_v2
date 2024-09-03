#!/usr/bin/python3
"""create the Tool model"""

from models.base_model import BaseModel, storage_type, Base
from sqlalchemy import Column, String

class Tool(BaseModel, Base):
    """create tools instances"""
    if storage_type == "db":
        __tablename__ = "tools"
        name = Column("name", String(128), nullable=False)
    else:
        name = ""

    def __init__(self, **kwargs):
        """
        instansiate a Tool instance
        and set all attribute passed of the form of kwargs
        """
        super().__init__()
        for key, val in kwargs.items():
            setattr(self, key, val)
