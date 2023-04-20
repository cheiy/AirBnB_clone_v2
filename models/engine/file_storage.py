#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return self.__objects
        cls_objects = {}
        for key, value in self.__objects.items():
            if cls == type(value):
                cls_objects.update({key: value})
        return cls_objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        dictionary = {}
        for key, value in self.__objects.items():
            dictionary[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(dictionary, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    val = eval(val["__class__"])(**val)
                    self.__objects[key] = val
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ Method deletes object from __objects, if object exists"""
        if obj is None:
            return
        key = obj.__class__.__name__ + '.' + obj.id
        if key in self.__objects:
            del self.__objects[key]

    def close(self):
        """Calls reload"""
        self.reload()
