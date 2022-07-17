import sqlalchemy as sa
import sqlalchemy.orm as so
from .base import Base


class UserLink(Base):
    url = sa.Column(sa.Text)
    short = sa.Column(sa.Text)
    user = sa.Column(sa.Integer, sa.ForeignKey('user.id'))


class Tag(Base):
    name = sa.Column(sa.Text)


association_table = sa.Table(
    "association",
    Base.metadata,
    sa.Column("user_link_id", sa.ForeignKey("left.id")),
    sa.Column("tag_id", sa.ForeignKey("right.id")),
)
