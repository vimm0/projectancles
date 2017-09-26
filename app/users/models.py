from sqlalchemy import Column, Integer, String, Text
from apistar import typesystem
from db_base import Base, BaseScheme


class UserScheme(BaseScheme):
    render_fields = ['id', 'first_name', 'last_name']
    properties = {
        "id": typesystem.integer(default=0),
        "first_name": typesystem.String,
        "last_name": typesystem.String,
        "password": typesystem.String
    }


class User(Base):
    __tablename__ = "users"
    _scheme = UserScheme

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    password = Column(Text)
