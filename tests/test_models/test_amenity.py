#!/usr/bin/env python3
"""Defines unittest for the Amenity model.

unittest classes:
    TestAmenity_instantiation
    TestAmenity_save
    TestAmenity_to_dict
"""
import unittest
import models
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    """Tests the instantiation of Amenity"""

    def test_no_args_instantiation(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_is_stored_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Amenity().id))


class TestAmenity_save(unittest.TestCase):
    """Tests the save method of Amenity"""

    def test_save(self):
        amn = Amenity()
        init_updated_at = amn.updated_at
        sleep(0.10)
        amn.save()
        self.assertLess(init_updated_at, amn.updated_at)


class TestAmenity_to_dict(unittest.TestCase):
    """Tests the to_dict method of Amenity"""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))
