from src.modules.message.models import Message
from src.extensions import ma


class MessageSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Message
