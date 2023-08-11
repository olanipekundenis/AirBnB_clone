#!/usr/bin/python3
"""BaseModel module"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """BaseModel class"""

    def __init__(self, *args, **kwargs):
        """Initialization of model"""
        if kwargs is not None and kwargs != {}:
            del kwargs["__class__"]
            for key in kwargs.keys():
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                            kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                            kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """string representation of an instance"""
        return "[{}] ({}) {}".format(
                type(self).__name__, self.id, self.__dict__)

    def save(self):
        """update the public instance attribute"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Serialize object to JSON"""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = type(self).__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
