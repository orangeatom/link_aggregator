import sqlalchemy.orm as so
import sqlalchemy as sa

Base = so.declarative_base()

class Base(Base):
    id = sa.Column(sa.Integer, primary_key=True)
    created_at = sa.Column(sa.DateTime, server_default=sa.func.now())