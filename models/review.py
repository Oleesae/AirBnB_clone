#!/usr/bin/python3
"""The Review Module"""
from models.base_model import BaseModel
from models import storage


class Review(BaseModel):
    """The Review class"""
    place_id = ""
    user_id = ""
    text = ""
