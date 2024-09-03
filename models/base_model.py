#!/usr/bin/python3
"""
create a BaseModel class
that is gonna be the parent of most of the models
"""

from uuid import uuid4
from datetime import datetime, timezone
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, DateTime
from models import storage_type

if storage_type == "db":
    Base = declarative_base()
else:
    Base = object

# if models.storage_type != "db":
class BaseModel:
    """set the common attributes for all child classes"""
    if storage_type == "db":
        id = Column("id", String(60), primary_key=True)
        created_at = Column("created_at", DateTime, nullable=False)
        updated_at = Column("updated_at", DateTime, nullable=False)

    def __init__(self, id=str(uuid4()),
                created_at=datetime.now(timezone.utc),
                updated_at=datetime.now(timezone.utc)):
        """Instatntiates a new BaseModel with id, created_at and updated_at"""
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        """
        string representation of an object with the follwoing format:
                                    [<class name>] (<self.id>) <self.__dict__>
                        return the above representation of the object
        """
        cls_name = self.__class__.__name__
        return f"[{cls_name}] ({self.id}) {self.__dict__}"


    def save(self):
        from models import storage
        """
        save the object in the storage engine
        after modifying the "updated_at" attribute to time now in UTC
        """
        self.updated_at = datetime.now(timezone.utc)
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        return a dict having the following keys and values:
        "__class__": class of the object
        "created_at": creation date in iso format
        "updated_at": update date in iso format
        """
        repr_dict = self.__dict__.copy()
        repr_dict["__class__"] = self.__class__.__name__
        repr_dict["created_at"] = self.created_at.isoformat()
        repr_dict["updated_at"] = self.updated_at.isoformat()
        if storage_type == "db":
            del repr_dict["_sa_instance_state"]
        return repr_dict
    
    def delete(self):
        """
        delete the passed instance from the storage
        and save chages to teh file storage
        """
        from models import storage

        storage.delete(self)
        storage.save()
