#!/usr/bin/python3
"""BaseModel module"""
import uuid
from datetime import datetime


class BaseModel:
    """BaseModel class"""

    def __init__(self, *args, **kwargs):
        """Initialization of model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """string representation of an instance"""
        return "[{}] ({}) {}".format(
                type(self).__name__, self.id, self.__dict__)

    def save(self):
        """update the public instance attribute"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Serialize object to JSON"""
        obj_dict = self.__dict__
        obj_dict.update({"__class__": type(self).__name__})
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_diict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
