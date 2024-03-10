#!/usr/bin/python3

"""
BaseModel - a class that defines all common
attributes/methods for other classes.
"""


import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """
    BaseModel - a class that defines all common
    attributes/methods for other classes.

    Public instance attributes:
    id: string assigned with an uuid.
    created_at: datetime assigned with the current datetime (at creation).
    updated_at: datetime - assign with the current datetime (at update).

    Public instance methods:
    save(self): updates the public instance attribute
                updated_at with the current datetime
    to_dict(self): returns a dictionary containing
                all keys/values of __dict__ of the instance.
    """
    def __init__(self, *args, **kwargs):
        """ __init__ - set up the initial state of an object."""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """ save - updates the public instance attribute
            updated_at with the current datetime"""
        updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ to_dict - returns a dictionary containing
            all keys/values of __dict__ of the instance"""
        _dict = self.__dict__.copy()
        _dict["__class__"] = self.__class__.__name__
        for key, value in _dict.items():
            if isinstance(value, datetime):
                _dict[key] = value.isoformat()

        return _dict

    def __str__(self):
        """ should print: [<class name>] (<self.id>) <self.__dict__> """
        return f"[{self.__class__.__name__}]({self.id}){self.__dict__}"
