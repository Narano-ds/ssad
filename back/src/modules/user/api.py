import email
from flask import Blueprint, jsonify, request
from flask_classful import FlaskView
from src.modules.user.models import User
from src.modules.user.schemas import UserSchema
from src.common.base_api import BaseAPI
from src.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user
from flask import session
import http


blueprint = Blueprint("user", __name__, url_prefix="/api")

class UserAPI(BaseAPI):
    route_base = 'users'
    model = User
    schema = UserSchema

    def post(self):
        username=request.json['username']
        password=request.json['password_hash']
        user = User.query.filter_by(username=username).first()
        if not user:
            new_User=User(username=username,password_hash=generate_password_hash(password, method='sha256'))
        db.session.add(new_User)
        db.session.commit()
        return{}
    def Login(self,methods=["POST"]):
        username=request.json['username']
        password=request.json['password_hash']

        user = User.query.filter_by(username=username).first()

        if not user or not check_password_hash(user.password_hash,password):
            return{}
        login_user(user)
        if "user" in session:
            user=session["user"]
        print (session)
        return {"username":user.username}
    
    def LogOut(self):
        session.pop("user",None)
        print (session)
        return{}
        
UserAPI.register(blueprint)




"""
    def index(self):
        user_list=User.query.all()
        serializer = self.schema(many=True)
        return jsonify( serializer.dump(user_list), http.HTTPStatus.OK)
   


"""
"""


class UserAPI(FlaskView):
    route_base="users"
    trailing_slash :None

    model= User
    
    def post(self):
        
        user_list = User.query.all()
        
        
        next_id=0
        for user in user_list:
            if next_id<user.id:
                next_id=user.id
        print (next_id)
        model =User(email = request.json['email'],id=next_id+1,password= request.json['password'],username=request.json['username'])
        verify = 0

        for user in user_list:
            if (model.email==user.email):
                verify =1 


        if verify==0:
            db.session.add(model)
            db.session.commit()
        return {'id':model.id}
UserAPI.register(blueprint)
    
    

#@blueprint.route("users")
#def index():
#    return {"data": [
#         {"name": "Someone", "email": "a@a.a"}
#         ]}

# @route(users/:id)
# def user(id):
#     get from db by id
# user -> update user
# add
# commit

# return render_template, user


"""