# -*- coding: utf-8 -*-

# Import standard library packages

# Import installed packages

from sqlalchemy import Column,  String
from app.core.db.base_class import Base

class Role (Base):
     __tablename__ = 'role'
     role_name = Column(String(200), nullable=True)

def __repr__(self):
    return f'{self.id} {self.role_name}'