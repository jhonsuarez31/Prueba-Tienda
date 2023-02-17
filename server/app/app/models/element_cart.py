# -*- coding: utf-8 -*-

# Import standard library packages

# Import installed packages

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from app.core.db.base_class import Base

class Element_Cart (Base):
     __tablename__ = 'element_cart'

     cart_id = Column(Integer, ForeignKey('element_cart.id'), index=True)
     cart = relationship('Element_Cart', foreign_keys=[cart_id])

     product_id = Column(Integer, ForeignKey('product.id'), index=True)
     product = relationship('Product', foreign_keys=[product_id]) 

     stock = (Column(Integer, nullable= True))

def __repr__(self):
    return f'{self.id}'