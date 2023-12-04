"""
    This file contains the BaseModel class, which serves as the base class for all models in the project.
"""
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """
    Base class for all models.
    """

    id = str(uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def __str__(self) -> str:
        """
        Returns a string representation of the object.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the 'updated_at' attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the object.
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
