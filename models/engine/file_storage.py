#!/usr/bin/python3
"""
The File Storage Module
"""
import json
import os


class FileStorage:
    """The FileStorage Class"""

    __file_path = 'filestorage.json'
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

        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r+", encoding="utf-8") as f:
            obj_j = json.load(f)
            FileStorage.__objects = obj_j
