#!/usr/bin/python3
"""Defines the BaseModel Class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Representation of the BaseModel for the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        timeform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(val, timeform)
                else:
                    self.__dict__[key] = val
        else:
            models.storage.new(self)

    def save(self):
        """Update the updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        repdict = self.__dict__.copy()
        repdict["created_at"] = self.created_at.isoformat()
        repdict["updated_at"] = self.updated_at.isoformat()
        repdict["__class__"] = self.__class__.__name__
        return repdict

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
