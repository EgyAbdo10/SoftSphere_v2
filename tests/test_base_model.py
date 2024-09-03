#!/usr/bin/python3
"""test base model class"""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import json

class test_BaseModel(unittest.TestCase):
    """test base model class by using unittests"""
    def test_common_attrs(self):
        """check common atributes in the BaseModel class"""
        b1 = BaseModel()
        self.assertIn("id", b1.__dict__.keys())
        self.assertIn("created_at", b1.__dict__.keys())
        self.assertIn("updated_at", b1.__dict__.keys())
        b2 = BaseModel(id="00-11-33")
        self.assertEqual("00-11-33", b2.id)
    
    def test_str(self):
        """test the string representation of the baseModel"""
        ...
    
    def test_to_dict(self):
        """test the to_dict method"""
        b3 = BaseModel("11-22")
        repr_dict = b3.to_dict()
        b3_dict = list(b3.__dict__.keys()) + ["__class__"]
        for key in repr_dict.keys():
            self.assertIn(key, b3_dict)

    def test_save_delete(self):
        """test save and delete method"""
        with open("file.json", "w") as f:
            ... # clear file
        b4 = BaseModel(id="50-3I3")
        b5 = BaseModel(id="uu-t42")
        b4.save()
        b5.save()
        with open("file.json", "r") as f:
            data = json.load(f)
            self.assertEqual(b4.to_dict(), data["BaseModel.50-3I3"])
            self.assertEqual(b5.to_dict(), data["BaseModel.uu-t42"])
        
        ############################

        b4.delete()
        with open("file.json", "r") as f:
            data  = json.load(f)
            self.assertNotIn("BaseModel.50-3I3", data.keys())
