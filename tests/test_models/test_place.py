#!/usr/bin/env python3
"""Defines unittest for the Place model.

unittest classes:
    TestPlace_instantiation
    TestPlace_save
    TestPlace_to_dict
"""
import unittest
import models
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace_instantiation(unittest.TestCase):
    """Tests the instantiation of Place"""

    def test_no_args_instantiation(self):
        self.assertEqual(Place, type(Place()))

    def test_new_instance_is_stored_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Place().id))


class TestPlace_save(unittest.TestCase):
    """Tests the save method of Place"""

    def test_save(self):
        plc = Place()
        init_updated_at = plc.updated_at
        sleep(0.10)
        plc.save()
        self.assertLess(init_updated_at, plc.updated_at)


class TestPlace_to_dict(unittest.TestCase):
    """Tests the to_dict method of Place"""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Place().to_dict()))
