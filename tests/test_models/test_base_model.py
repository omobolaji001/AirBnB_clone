#!/usr/bin/env python3
"""Defines unittest for the base model.

unittest classes:
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
"""
import unittest
import models
from models.base_model import BaseModel
from datetime import datetime
from time import sleep


class TestBaseModel_instantiation(unittest.TestCase):
    """Tests the instatiation of BaseModel."""

    def test_no_args_instantiation(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_new_instance_is_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_instances_has_unique_id(self):
        model_1 = BaseModel()
        model_2 = BaseModel()
        self.assertNotEqual(model_1.id, model_2.id)

    def test_two_models_has_different_created_at(self):
        model_1 = BaseModel()
        sleep(0.10)
        model_2 = BaseModel()
        self.assertLess(model_1.created_at, model_2.created_at)

    def test_two_models_has_different_updated_at(self):
        model_1 = BaseModel()
        sleep(0.10)
        model_2 = BaseModel()
        self.assertLess(model_1.updated_at, model_2.updated_at)


class TestBaseModel_save(unittest.TestCase):
    """Unittest for the save method of BaseModel."""

    def test_save(self):
        model = BaseModel()
        init_updated_at = model.updated_at
        sleep(0.10)
        model.save()
        self.assertLess(init_updated_at, model.updated_at)


class TestBaseModel_to_dict(unittest.TestCase):
    """Unittest for to_dict method of BaseModel."""

    def test_to_dict_type(self):
        model = BaseModel()
        self.assertTrue(dict, type(model.to_dict()))

    def test_to_dict_time_attributes_are_str(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(str, type(model_dict["created_at"]))
        self.assertEqual(str, type(model_dict["updated_at"]))


if __name__ == "__main__":
    unittest.main()
