from sqlalchemy import Column, String
from app.core.db.base_class import Base


class TokenBlocklist(Base):  
    __tablename__ = 'token_block_list'
    jti = Column(String(50), nullable=False, index=True)
