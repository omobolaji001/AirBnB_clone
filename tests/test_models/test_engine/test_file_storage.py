#!/usr/bin/env python3
"""Defines unittest for models/engine/file_storage.py"""
import unittest
import models
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class TestFileStorage_instantiation(unittest.TestCase):
    """Tests the instantiation of FileStorage"""

    def test_FileStorage_instantiation_without_args(self):
        self.assertEqual(FileStorage, type(FileStorage()))
