import json
import os
from models.base_model import BaseModel
from models.user import User

class FileStorage:

    def __init__(self):

        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        serialized_objects = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(serialized_objects, f)



    
    def reload(self):
        """
        Deserializes the JSON file to __objects
        Only if the JSON file (__file_path) exists; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                if os.stat(self.__file_path).st_size == 0:
                    pass
                else:
                    data = json.load(f)
                    for key, obj_data in data.items():
                        class_name, obj_id = key.split('.')
                        cls = globals()[class_name]
                        obj_instance = cls(**obj_data)
                        self.__objects[key] = obj_instance
