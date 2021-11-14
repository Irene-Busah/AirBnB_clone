#!/usr/bin/python3

"""The User class inherits from the BaseModel class"""

from base_model import BaseModel


class User(BaseModel):
    """Initializing the instance attributes of the class"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
