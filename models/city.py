#!/usr/bin/python3
"""The City Module"""
from models.base_model import BaseModel
from models import storage


class City(BaseModel):
    """The City class"""
    state_id = ""
    name = ""
