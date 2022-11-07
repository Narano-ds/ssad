from src.modules.user.models import User
from src.extensions import ma


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
