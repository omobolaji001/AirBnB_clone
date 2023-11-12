#!/usr/bin/env python3
# FileStorage class
"""import modules here"""
import json
from models.base_model import BaseModel


class FileStorage:
    """ serializes instances to JSON file and
    deserializes JSON file to instances
    """
    __file_path = "file_storage.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return (type(self).__objects)

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        dic = type(self).__objects
        dic["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """serializes __objects to JSON file __file_path."""
        dic = type(self).__objects
        obj_dic = {obj: dic[obj].to_dict() for obj in dic.keys()}

        with open(type(self).__file_path, mode='w', encoding='utf-8') as file:
            json.dump(obj_dic, file)

    def reload(self):
        """deserializes JSON file __file_path to __objects if it exists"""
        try:
            with open(type(self).__file_path, 'r', encoding='utf-8') as file:
                json_load = json.load(file)

            for v in json_load.values():
                model_name = v["__class__"]
                self.new(eval(model_name)(**v))

        except FileNotFoundError:
            pass
