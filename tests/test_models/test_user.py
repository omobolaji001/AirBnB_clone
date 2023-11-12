#!/usr/bin/env python3
"""Defines unittest for the User model.

unittest classes:
    TestUser_instantiation
    TestUser_save
    TestUser_to_dict
"""
import unittest
import models
from datetime import datetime
from time import sleep
from models.user import User


class TestUser_instantiation(unittest.TestCase):
    """Tests the instantiation of User"""

    def test_no_args_instantiation(self):
        self.assertEqual(User, type(User()))

    def test_new_instance_is_stored_in_objects(self):
        self.assertIn(User(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(User().id))


class TestUser_save(unittest.TestCase):
    """Tests the save method of User"""

    def test_save(self):
        customer = User()
        init_updated_at = customer.updated_at
        sleep(0.10)
        customer.save()
        self.assertLess(init_updated_at, customer.updated_at)


class TestUser_to_dict(unittest.TestCase):
    """Tests the to_dict method of User"""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(User().to_dict()))
