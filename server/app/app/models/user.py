# -*- coding: utf-8 -*-

# Import standard library packages

# Import installed packages

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from app.core.db.base_class import Base


class User(Base):
    __tablename__ = 'user'
    
    name = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False)
    password = Column(String(200), nullable=False)

    role_id = Column(Integer, ForeignKey('role.id'), index=True)
    role = relationship('Role', foreign_keys=[role_id], )

def __repr__(self):
    return f'{self.email}'