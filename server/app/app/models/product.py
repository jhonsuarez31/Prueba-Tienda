# -*- coding: utf-8 -*-

# Import standard library packages

# Import installed packages

from sqlalchemy import Column,  String, Integer
from app.core.db.base_class import Base

class Product (Base):
     __tablename__ = 'product'
     name = Column(String(200), nullable=True)
     description = (Column(String(500), nullable=True))
     price = (Column(Integer, nullable=True))   
     amount = (Column(Integer, nullable=True))
     stock = (Column(Integer, nullable= True))
     

def __repr__(self):
    return f'{self.id} {self.name}'