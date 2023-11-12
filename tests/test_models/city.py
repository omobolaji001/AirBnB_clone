#!/usr/bin/python3
"""Import Module Here"""
import unittest
from models.city import City


class test_city(unittest.TestCase):
    """Public Class Attrbute"""
    
    def test_module(self):
        """testing the module """
        module = (__import__("models.city").city.__doc__)
        self.assertGreater(len(module), 0)

    def test_class(self):
        """test class """
        testClass = (__import__("models.city").city.City.__doc__)
        self.assertGreater(len(testClass), 0)

    def test_name(self):
        """ test name class attribute """
        city = City()
        self.assertIs(type(city.name), str)
    
    def test_id(self):
        """test the id attribute of the class """
        city = City()
        self.assertIs(type(city.state_id), str)

if __name__ == "__main__":
    unittest.main()
