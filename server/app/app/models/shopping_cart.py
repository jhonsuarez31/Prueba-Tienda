# -*- coding: utf-8 -*-

# Import standard library packages

# Import installed packages

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from app.core.db.base_class import Base

class Shopping_Card(Base):
    __tablename__ = 'shopping_card'

    user_id = Column(Integer, ForeignKey('user.id'), index=True)
    role = relationship('User', foreign_keys=[user_id])

def __repr__(self):
    return f'{self.id}'
