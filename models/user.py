#!/usr/bin/python3
"""
This file contains the user class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User classs
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
