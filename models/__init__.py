#!/usr/bin/python3
"""reload storage every time models are imported"""
from os import getenv

storage_type = getenv("SOS_STORAGE_TYPE")
if storage_type == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
