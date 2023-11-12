#!/usr/bin/python3
""" Import Module Here """
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases """


    def test_module(self):
        """module test"""
        module = (__import__.("models.amenity").amenity.__doc__)
        self.assertGreater(len(module), 0)

    def test_class(self):
        """class test """
        class_test = (__import__.("models.amenity").amenity.Amenity.__doc__)
        self.assertGreater(len(class_test), 0)

    def test_attr(self):
        """Attributes test """
        amenity = Amenity()
        self.assertIs(type(amenity.name), str)

if __name__ == "__main__":
    unittest.main()
