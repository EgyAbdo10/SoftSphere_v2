#!/usr/bin/python3
"""create the Project model"""

from models.base_model import BaseModel, Base, storage_type
from sqlalchemy import (String, Column,
                        TEXT, ForeignKey, Table)
from sqlalchemy.orm import relationship
from models.tools import Tool

if storage_type == "db":
    project_tools = Table("project_tools", Base.metadata,
                          Column("project_id", ForeignKey("projects.id", 
                                                          onupdate="CASCADE",
                                                          ondelete="CASCADE"),
                                  primary_key=True),
                          Column("tool_id", ForeignKey("tools.id",
                                                       onupdate="CASCADE",
                                                       ondelete="CASCADE"),
                                 primary_key=True),
                          Column("tool_version", String(60)
                                ))

class Project(BaseModel, Base):
    """create the Project model"""
    if storage_type == "db": # meaning the storage engine is db
        __tablename__ = "projects"
        name = Column("name", String(60), nullable=False)
        description = Column("description", String(255), nullable=True)
        video_url = Column("video_url", String(255), nullable=True)
        #   video_url --> if the image is on device use the following naming convention:
        #    "project_id-0.vid_extension",
        images = Column("images", TEXT, nullable=True)
        # JSON NULL, ---> for passing a list of images urls
        # --> if the image is on device use the following naming convention:
            # "project_id-img_no.img_extension"
        category_id = Column(String(60), ForeignKey("categories.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        tools = relationship("Tool", secondary="project_tools", viewonly=False)

        def to_dict(self):
            tool_ids = [tool.id for tool in self.tools]
            dict_repr = super().to_dict()
            dict_repr["tools"] = tool_ids
            return dict_repr

    else:
        name = ""
        description = ""
        video_url = ""
        images = []
        category = ""
        user_id = ""
        tools = []
        
        @property
        def owner(self):
            return getattr(self, "owner", None)
                    

    def __init__(self, **kwargs):
        """
        instansiate a Project instance
        and set all attribute passed of the form of kwargs
        """
        super().__init__()
        for key, val in kwargs.items():
            setattr(self, key, val)
