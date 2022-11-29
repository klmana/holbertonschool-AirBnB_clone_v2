#!/usr/bin/python3
"""
  Module contains the engine for the db storage.
"""

from models.review import Review
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.user import User
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
import models
import json
import os


class DBStorage():
    """
      Attributes will get system info to start engine.
    """
    __engine = None
    __session = None

    def __init__(self):
        """
          Creates the engine for SQLALCHEMY.
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.getenv('HBNB_MYSQL_USER'),
            os.getenv('HBNB_MYSQL_PWD'),
            os.getenv('HBNB_MYSQL_HOST'),
            os.getenv('HBNB_MYSQL_DB'),
            pool_pre_ping=True))

        ## Drop all tables is test_user for QOL.
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """
          get dictionary of all objects
        """

        if cls is None:
            all_list = []
            for x in BaseModel.__subclasses__():
                all_list.extend(self.__session.query(x).all())
            return {"{}.{}".format(type(obj).__name__, obj.id): obj
                    for obj in all_list}

        if type(cls) is str:
            cls = eval(cls)

        return {"{}.{}".format(type(obj).__name__, obj.id): obj
                for obj in self.__session.query(cls).all()}

    def new(self, obj):
        """
          insert new object in current database session
        """
        self.__session.add(obj)

    def save(self):
        """
          commit changes to database
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
          delete from current database session
        """

        if obj is not None:
            all_instances = self.__session.query(obj.__class__.__name__).all()
            for instance in all_instances:
                if obj == instance:
                    self.__session.delete(obj)
                    self.save()                  



    def reload(self):
        """
          Reload the database
        """

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """
         call remove() method on the private session attribute
         (self.__session) or close() on the class Session
        """
        self.__session.close()
