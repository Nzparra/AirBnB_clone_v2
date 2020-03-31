#!/usr/bin/python3
"""This is the user class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, MetaData


class User(BaseModel, Base):
    """This is the class for user
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
    """
    __tablename__ = 'users'
    email = Column(String(128, nullalbe=False))
    password = Column(String(128, nullalbe=False))
    first_name = Column(String(128, nullalbe=False))
    last_name = Column(String(128, nullalbe=False))
