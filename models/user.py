#!/usr/bin/python3
"""User module"""
from models.base_model import BaseModel
from models import storage

class User(BaseModel):
    """The User class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
