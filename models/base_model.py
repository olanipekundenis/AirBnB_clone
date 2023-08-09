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
        print("[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__))

    def save(self):
        """update the public instance attribute"""
        self.updated_at = datetime.now()
