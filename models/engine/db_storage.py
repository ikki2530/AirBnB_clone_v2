#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.state import State
from models.city import City

class DBStorage:
    __engine = None
    __session = None
    clases = [State, City]

    def __init__(self):
        self.__engine = create_engine(
            "{}+{}://{}:{}@{}:3306/{}".format(
            'mysql', 'mysqldb', getenv('HBNB_MYSQL_USER'),
            getenv('HBNB_MYSQL_PWD'), getenv('HBNB_MYSQL_HOST'),
            getenv('HBNB_MYSQL_DB')), pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        new_dict = {}
        if cls is not None:
            query = self.__session().query(cls).all()
        else:
            for clase in self.clases:
                query = self.__session().query(clase).all()
                print(query)


    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)

        self.__session = scoped_session(sessionmaker(
            bind=self.__engine, expire_on_commit=False
        ))
