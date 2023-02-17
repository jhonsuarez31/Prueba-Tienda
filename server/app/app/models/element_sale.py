# -*- coding: utf-8 -*-

# Import standard library packages

# Import installed packages

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from app.core.db.base_class import Base

class Element_sale (Base):
     __tablename__ = 'element_sale'

     
     sale_id = Column(Integer, ForeignKey('sale.id'), index=True)
     user = relationship('Sale', foreign_keys=[sale_id]) 

     product_id = Column(Integer, ForeignKey('product.id'), index=True)
     product = relationship('Product', foreign_keys=[product_id]) 

     amount = (Column(Integer, nullable= True))
     unit_price = (Column(Integer, nullable= True))
def __repr__(self):
    return f'{self.id}'