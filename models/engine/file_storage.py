#!/usr/bin/python3

"""The FileStorage module stores the classes and their management
It serializes instances to a JSON file and deserializes JSON file to instances
"""

import json
from os import path

from models.base_model import BaseModel


class FileStorage:
    """
    Private class attributes: __file_path - path to the JSON file __objects - stores all objects by <class
    name>.id Public instance methods: all(self) - returns the dictionary __objects new(self) - sets in __objects the
    obj with key <obj class name>.id save(self): serializes __objects to the JSON file (path: __file_path) reload(
    self): deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise,
    do nothing. If the file doesn’t exist, no exception should be raised)
    """

    __file_path = 'objects.json'
    __objects = {}

    def all(self):
        """returns the dictionary of __objects"""
        return self.__objects

    def new(self, obj):
        """sets __objects the obj with the key <obj class name>.id"""
        keys = obj.__class__.name__ + '.' + obj.id
        self.__objects[keys] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_dictionary = {}
        for key, value in self.__objects.items():
            json_dictionary[key] = value.to_dict()
        with open(self.__file_path, mode='w', encoding='utf-8') as file:
            file.write(json.dumps(json_dictionary))

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise,
        do nothing"""
        if path.exists(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as file:
                json_dictionary = json.loads(file.read())
                for key, value in json_dictionary.items():
                    self.__objects[key] = eval(value['__class__'])(**value)





