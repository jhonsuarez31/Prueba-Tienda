# import external libraries
import datetime

# sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime, Boolean


class CustomBase(object):
    __abstract__ = True
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now(), index=True, nullable=False)
    updated_at = Column(DateTime, nullable=True)

    def serialize(self):
        return {
            'id': self.id,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }


Base = declarative_base(cls=CustomBase)


