#!/usr/bin/python3
"""The Amenity Module"""
from models.base_model import BaseModel
from models import storage


class Amenity(BaseModel):
    """The Amenity class"""
    name = ""
