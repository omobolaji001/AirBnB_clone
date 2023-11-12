#!/usr/bin/python3
"""Import module """
from models.base_model import BaseModel


class User(BaseModel):
    """Public clss attribute """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
