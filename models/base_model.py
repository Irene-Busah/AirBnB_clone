#!/usr/bin/python3

""" The BaseModel takes care of the initialization, serialization
    and deserialization
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Instantiating the instance methods and attributes of the BaseModel class
    id: assign with an uuid when an instance is created
        use uuid.uuid4() to generate unique id(needs to be convert to a string)
        the goal is to have a unique id for each BaseModel
    created_at: assign with the current datetime when the instance is created
    updated_at: assign with the current datetime when an instance is created
    and it will be updated every time you change your object
    """

    def __init__(self, *args, **kwargs):
        """Instantiating the instance attributes of the class"""
        if kwargs:
            for arg, value in kwargs.items():
                if arg in ('created_at', 'updated_at'):
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if arg != '__class__':
                    setattr(self, arg, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            from models.engine import file_storage
            models.engine.file_storage.new(self)

    def __str__(self):
        return '[{0}] ({1}) {2}'.format(self.__class__.__name__,
                                        self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at"""
        self.updated_at = datetime.now()
        models.engine.save()

    def to_dict(self):
        """return a dictionary containing all keys/values of __dict__"""
        new_dict = {}
        for key, value in self.__dict__.items():
            if key == 'created_at' or key == 'updated_at':
                new_dict[key] = value.isoformat()
            else:
                new_dict[key] = value
        new_dict['__class__'] = type(self).__name__
        return new_dict
