#!/usr/bin/env python3
# Base_model class
"""import modules here """
import uuid
from datetime import datetime
import models


class BaseModel:
    """basemodel to be inherited by other classes """

    def __init__(self, *args, **kwargs):
        """to be initialised wiith"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == '__class__':
                    pass
                elif k == 'created_at':
                    self.created_at = datetime.fromisoformat(v)
                elif k == 'updated_at':
                    self.updated_at = datetime.fromisoformat(v)
                else:
                    self.__dict__[k] = v
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """printing the class """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ updates attribute 'updated_at' with the current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__"""
        dic = self.__dict__.copy()
        dic['__class__'] = type(self).__name__
        dic['created_at'] = (self.created_at).isoformat()
        dic['updated_at'] = (self.updated_at).isoformat()

        return dic
