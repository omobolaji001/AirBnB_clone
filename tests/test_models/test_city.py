#!/usr/bin/env python3
"""Defines unittest for the City model.

unittest classes:
    TestCity_instantiation
    TestCity_save
    TestCity_to_dict
"""
import unittest
import models
from datetime import datetime
from time import sleep
from models.city import City


class TestCity_instantiation(unittest.TestCase):
    """Tests the instantiation of City"""

    def test_no_args_instantiation(self):
        self.assertEqual(City, type(City()))

    def test_new_instance_is_stored_in_objects(self):
        self.assertIn(City(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(City().id))


class TestCity_save(unittest.TestCase):
    """Tests the save method of City"""

    def test_save(self):
        new_york = City()
        init_updated_at = new_york.updated_at
        sleep(0.10)
        new_york.save()
        self.assertLess(init_updated_at, new_york.updated_at)


class TestCity_to_dict(unittest.TestCase):
    """Tests the to_dict method of City"""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(City().to_dict()))
