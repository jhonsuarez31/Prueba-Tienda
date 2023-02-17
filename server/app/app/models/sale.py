# -*- coding: utf-8 -*-

# Import standard library packages

# Import installed packages

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from app.core.db.base_class import Base

class Sale (Base):
     __tablename__ = 'sale'

     
     user_id = Column(Integer, ForeignKey('user.id'), index=True)
     user = relationship('User', foreign_keys=[user_id]) 

     date = (Column(DateTime, nullable= True))

def __repr__(self):
    return f'{self.id}'