#!/usr//bn/python3
#Base_model class
"""import modules here """
import uuid
from datetime import datetime


class BaseModel:
    """basemodel to be inherited by other classes """

    def __init__(self):
        """to be initialised wiith"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated at = datetime.now()


