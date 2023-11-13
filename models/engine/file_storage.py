#!/usr/bin/python3
"""
The File Storage Module
"""
import json
import os


class FileStorage:
    """The FileStorage Class"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""

        return FileStorage.__objects

    def new(self, obj):
        """Sets  in __objects the obj with key <obj class name>.id"""

        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Seriralizes __objects to the JSON file path"""

        with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def reload(self):
        """Deserializes the JSON file to __objects
        raising no exceptions if not exist"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        from models.place import Place

        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r+", encoding="utf-8") as f:
            obj_j = json.load(f)
            for v in obj_j.values():
                cl = v['__class__']
                del v['__class__']
                self.new(eval(cl)(**v))
