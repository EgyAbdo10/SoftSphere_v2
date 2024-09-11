#!/usr/bin/python3
"""create the User model"""


from models.base_model import BaseModel, Base, storage_type
from sqlalchemy import Column, String, Enum
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """create the user model"""
    if storage_type == "db":
        __tablename__ = "users"
        first_name = Column("first_name", String(60), nullable=False)
        last_name = Column("last_name", String(60), nullable=False)
        user_type = Column("user_type", Enum('developer', 'client', "employer"), nullable=False)
        username = Column("username", String(60), nullable=False, unique=True)
        password = Column("password", String(128), nullable=False)
        email = Column("email", String(128), nullable=False, unique=True)
        projects = relationship("Project", backref="owner", cascade="all, delete, delete-orphan")
        
    else:
        first_name = ""
        last_name = ""
        user_type = ""
        username = ""
        password = ""
        email = ""
        
        @property
        def projects(self):
            """get all projectsof a certain user"""
            from models import storage
            projects = storage.all("Project").values()
            user_projects = []
            for project in projects:
                if project.user_id == self.id:
                    user_projects.append(project)
            return user_projects
            
    def __init__(self, **kwargs):
        """
        create user instances
        """
        super().__init__()
        for key, val in kwargs.items():
            setattr(self, key, val)
