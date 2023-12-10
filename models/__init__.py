#!/usr/bin/python3
"""
    Defines the entry point of the command interpreter
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()

storage.reload()
