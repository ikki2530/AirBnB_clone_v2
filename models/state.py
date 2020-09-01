#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models.city import City
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
        """get all cities
        """
        cities = models.storage.all(City)
        city_l = []
        for i in cities.values():
            if self.id == i.state_id:
                city_l.append(i)
        return city_l
