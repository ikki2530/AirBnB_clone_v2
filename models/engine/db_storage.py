#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """This class manages storage of db"""
    __engine = None
    __session = None
    clases = [State, City, User, Place, Review, Amenity]

    def __init__(self):
        self.__engine = create_engine("{}+{}://{}:{}@{}:3306/{}".format(
            'mysql', 'mysqldb', getenv('HBNB_MYSQL_USER'),
            getenv('HBNB_MYSQL_PWD'), getenv('HBNB_MYSQL_HOST'),
            getenv('HBNB_MYSQL_DB')), pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        new_dict = {}
        if cls is not None:
            query = self.__session().query(cls).all()
            # creating the dictionary
            for obj in query:
                delattr(obj, '_sa_instance_state')
                cls_name = obj.__class__.__name__
                obj_id = obj.id
                key = cls_name + "." + obj_id
                new_dict[key] = obj
            return new_dict
        else:
            for clase in self.clases:
                query = self.__session().query(clase).all()
                for obj in query:
                    delattr(obj, '_sa_instance_state')
                    cls_name = obj.__class__.__name__
                    obj_id = obj.id
                    key = cls_name + "." + obj_id
                    new_dict[key] = obj
            return new_dict

    def new(self, obj):
        """Adds new object to db"""
        self.__session.add(obj)

    def save(self):
        """Saves data in db"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deleting an object from db"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Loads storage dictionary from db"""
        Base.metadata.create_all(self.__engine)

        self.__session = scoped_session(sessionmaker(
            bind=self.__engine, expire_on_commit=False
        ))
