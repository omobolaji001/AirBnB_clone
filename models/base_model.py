#!/usr//bn/python3
#Base_model class
"""import modules here """
import uuid
from datetime import datetime


class BaseModel:
    """basemodel to be inherited by other classes """

    def __init__(self):
        """to be initialised wiith"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """printing the class """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
