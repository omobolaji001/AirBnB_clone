#!/usr/bin/python3
"""Import Module Here """
from models.base_model import BaseModel


class Review(BaseModel):
    """Public class Attrbute """
    place_id = ""
    user_id = ""
    text = ""
