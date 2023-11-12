#!/usr/bin/python3
"""Import Modules Here """
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """test cases """


    def review_module(self):
        """test module """
        module = (__import__("models.review").review.__doc__)
        self.assertGreater(len(module), 0)

    def test_class(self):
        """test class """
        review_class = (__import__.("models.review").review.Review.__doc__)
        self.assertGreater(len(review_class), 0)

    def review_attr(self):
        """test attribute """
        review = Review()
        self.assertIs(type(review.place_id), str)
        self.assertIs(type(review.user_id), str)
        self.assertIs(type(review.text), str)

if __name__ == "__main__":
    unittest.main()
