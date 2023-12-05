#!/usr/bin/python3
"""
this file contains the class FileStorage
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """
    serializes instances to a JSON file and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        objects_dict = {}
        for key, obj in self.__objects.items():
            objects_dict[key] = obj.to_dict()

        with open(FileStorage.__file_path, "w") as f:
            json.dump(objects_dict, f, indent=4)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path, "r") as f:
                new_objs = json.load(f)

            for key, value in new_objs.items():
                class_name = value["__class__"]
                del value["__class__"]
                self.new(eval(class_name)(**value))
        except FileNotFoundError:
            pass
