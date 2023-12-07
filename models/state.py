#!/usr/bin/python3
"""Defines the State Class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Represents a state.

    Attributes (attrs):
        name (str): The name of the state.
    """

    name = ""
