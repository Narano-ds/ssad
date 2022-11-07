from enum import unique
from importlib.resources import contents
from src.extensions import db
from src.common.base_model import BaseModel
# from src.app import bcrypt

class Message(BaseModel):
    __tablename__ = 'messages'

    id = db.Column(db.Integer(), primary_key=True)
    content=db.Column(db.String(),nullable=False)
    owner=db.Column(db.String(),nullable=False)
    sent_to=db.Column(db.String(),nullable=False)
    


