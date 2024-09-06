#!/usr/bin/python3
"""apply a database storage to all models"""

from os import getenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.category import Category
from models.project import Project
from models.users import User
from models.tools import Tool

cls_names = {"Category": Category, "Project": Project,
             "Tool": Tool, "User": User}

class DBStorage:
    """create a db storage instances"""

    __engine = None # create_engine(f"mysql+mysqldb://{user}:{password}@{host}/{db}", pool_pre_ping=True)
    __session = None

    def __init__(self):
        """initialze a db storage instance"""
        user = getenv("SOS_USR")
        if not user:
            user = "SOS_user"
        passwd = getenv("SOS_PWD")
        if not passwd:
            passwd = "SOS_password"
        host = getenv("SOS_HOST")
        if not host:
            host = "localhost"
        db = getenv("SOS_DB")
        if not db:
            db = "SOS_db_dev"
        
        
        self.__engine = create_engine(
            f"""mysql+mysqldb://{user}:{passwd}@{host}/{db}""",
            pool_pre_ping=True)


    def all(self, cls=None):
        """get all objects in a dict format
        cls: the class itself or its name
        """
        new_dict = {}

        if cls in cls_names.keys():
            cls = cls_names[cls]

        if cls in cls_names.values():
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = obj.__class__.__name__ + "." + str(obj.id)
                new_dict[key] = obj

        else:
            for cls in cls_names.values():
                objs = self.__session.query(cls).all()
                for obj in objs:
                    key = obj.__class__.__name__ + "." + str(obj.id)
                    new_dict[key] = obj

        return new_dict
    
    def new(self, obj):
        """
        add the new object to the current session
        """
        self.__session.add(obj)

    def save(self):
        """
        commit all added objects to the current session
        """
        self.__session.commit()

    def delete(self, obj):
        """delete an object from the db"""
        try:
            self.__session.delete(obj)
            self.__session.commit()
            return True
        except:
            return False
    
    def reload(self):
        """
        create a scoped_session and assign it to __session
        and create all tables of the datebase
        """
        Base.metadata.create_all(bind=self.__engine, checkfirst=True)
        sessionFactory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        # to ensure thread-safe management sessions
        self.__session = scoped_session(sessionFactory)
        

    def find(self, cls_name, id):
        """search anf find objects by class and id of an object"""
        obj = self.__session.query(
                cls_names[cls_name]).filter_by(id=id).first()
        return obj
    
    def count(self, cls_name=None):
        """
        count all objects of a class or 
        count all objects from all classes
        """
        count = 0
        if cls_name in cls_names:
            count = len(self.all(cls_name))
        else:
            for cls_name in cls_names:
                count += len(self.all(cls_name))
        return count

    def close(self):
        """close session"""
        self.__session.close()