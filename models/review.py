#!/usr/bin/python3

"""The Review class inherits from the BaseModel class"""

from base_model import BaseModel


class Review(BaseModel):
    """Initializing the instance attributes
    place_id: empty string
    user_id : empty string
    text: empty string
    """
    place_id = ''
    user_id = ''
    text = ''
