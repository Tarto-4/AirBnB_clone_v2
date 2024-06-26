#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from datetime import datetime
import models

Base = declarative_base()

class BaseModel:
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            if key != "_sa_instance_state":
                setattr(self, key, value)
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.utcnow()

    def save(self):
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        models.storage.delete(self)

    def to_dict(self):
        dict_ = self.__dict__.copy()
        dict_['created_at'] = dict_['created_at'].isoformat()
        dict_['updated_at'] = dict_['updated_at'].isoformat()
        dict_.pop('_sa_instance_state', None)
        return dict_