from enum import unique
from src.extensions import db
from src.common.base_model import BaseModel
# from src.app import bcrypt
from flask_login import UserMixin

class User(UserMixin,BaseModel):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(),unique=True )
    password_hash = db.Column(db.String(),nullable=False)


