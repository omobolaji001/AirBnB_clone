#!/usr/bin/env python3
"""Defines unittest for the Review model.

unittest classes:
    TestReview_instantiation
    TestReview_save
    TestReview_to_dict
"""
import unittest
import models
from datetime import datetime
from time import sleep
from models.review import Review


class TestReview_instantiation(unittest.TestCase):
    """Tests the instantiation of Review"""

    def test_no_args_instantiation(self):
        self.assertEqual(Review, type(Review()))

    def test_new_instance_is_stored_in_objects(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Review().id))


class TestCity_save(unittest.TestCase):
    """Tests the save method of Review"""

    def test_save(self):
        rvw = Review()
        init_updated_at = rvw.updated_at
        sleep(0.10)
        rvw.save()
        self.assertLess(init_updated_at, rvw.updated_at)


class TestReview_to_dict(unittest.TestCase):
    """Tests the to_dict method of Review"""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Review().to_dict()))
