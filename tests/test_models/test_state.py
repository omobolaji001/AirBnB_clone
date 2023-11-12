#!/usr/bin/env python3
"""Defines unittest for the State model.

unittest classes:
    TestState_instantiation
    TestState_save
    TestState_to_dict
"""
import unittest
import models
from datetime import datetime
from time import sleep
from models.state import State


class TestState_instantiation(unittest.TestCase):
    """Tests the instantiation of State"""

    def test_no_args_instantiation(self):
        self.assertEqual(State, type(State()))

    def test_new_instance_is_stored_in_objects(self):
        self.assertIn(State(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(State().id))


class TestState_save(unittest.TestCase):
    """Tests the save method of State"""

    def test_save(self):
        state = State()
        init_updated_at = state.updated_at
        sleep(0.10)
        state.save()
        self.assertLess(init_updated_at, state.updated_at)


class TestState_to_dict(unittest.TestCase):
    """Tests the to_dict method of State"""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(State().to_dict()))
