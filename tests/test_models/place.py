#!/usr/bin/python3
"""Import Module here """
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """public class attribute """


    def test_module(self):
        """test the module """
        place_module = (__import__("models.place").place.__doc__)
        self.assertGreater(len(place_module), 0)

    def test_class(self):
        """test class """
        place_class = (__import__("models.place").place.Place.__doc__)
        self.assertGreater(len(place_class), 0)

    def test_attribute(self):
        """test class attributes """
        place = Place()
        self.assertIs(type(place.name), str)
        self.assertIs(type(place.city_id), str)
        self.assertIs(type(place.user_id), str)
        self.assertIs(type(place.description), str)
        self.assertIs(type(place.number_rooms), int)
        self.assertIs(type(place.number_bathrooms), int)
        self.assertIs(type(place.max_guest), int)
        self.assertIs(type(place.price_by_night), int)
        self.assertIs(type(place.latitude), float)
        self.assertIs(type(place.longitude), float)
        self.assertIs(type(place.amenity_ids), list)

if __name__ == "__main__":
    unittest.main()
