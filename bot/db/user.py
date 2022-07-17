import sqlalchemy as sa

from .base import Base

class User(Base):
    user_id: int = sa.Column(...)
    state: str = sa.Column(sa.String)
