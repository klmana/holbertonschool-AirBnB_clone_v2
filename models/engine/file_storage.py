#!/usr/bin/python3
"""
  This module defines a class to manage file storage for hbnb clone
"""
from models.review import Review
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.user import User
from models.base_model import BaseModel
import json

classes = {
    'BaseModel': BaseModel, 'User': User, 'Place': Place,
    'State': State, 'City': City, 'Amenity': Amenity,
    'Review': Review
}


class FileStorage:
    """
      This class manages storage of hbnb models in JSON format
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """
          Returns a dictionary of models currently in storage
        """
        cls_dict = {}
        if cls is not None:
            '''Check to see if cls exists in filestorage & add to dict.'''
            for k, v in self.__objects.items():
                if cls == v.__class__.__name__ or cls == v.__class__:
                    cls_dict[k] = v
            return cls_dict
        else:
            return FileStorage.__objects

    def new(self, obj):
        """
          Adds new object to storage dictionary
        """
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """
          Saves storage dictionary to file
        """
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """
          Loads storage dictionary from file
        """
        try:
            with open(FileStorage.__file_path, encoding="UTF8") as fd:
                FileStorage.__objects = json.load(fd)
            for key, val in FileStorage.__objects.items():
                class_name = val["__class__"]
                class_name = models.classes[class_name]
                FileStorage.__objects[key] = class_name(**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
          Delete an object if it exists in Filestroage
        """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects.pop(key)
            self.save()
        else:
            return

    def close(self):
        """
          Call reload() method for deserializing the JSON file to objects
        """
        self.reload()
