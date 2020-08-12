#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    # name = ""
    __tablename__ = 'states'
    if os.environ.get("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all,delete")

    @property
    def cities(self):
        """ the getter method for the cities """
        from models import storage
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            return
        cities = []
        filestorage = storage.FileStorage_objects
        for key, value in filestorage.items():
            lista = key.split()
            if lista[0] == "City":
                if value.to_dict()["state_id"] == self.id:
                    cities.append(value)
        return cities
