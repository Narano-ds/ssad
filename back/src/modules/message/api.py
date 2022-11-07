import email
from flask import Blueprint, jsonify, request
from flask_classful import FlaskView
from src.modules.user.models import User
from src.modules.message.models import Message
from src.modules.message.schemas import MessageSchema
from src.common.base_api import BaseAPI
from src.extensions import db
from itsdangerous import Serializer
import http
from src.modules.message.cryptage.Miroire import *
from src.modules.message.cryptage.cesar import *
from src.modules.message.cryptage.affine import *
from src.modules.message.cryptage.decalageGaucheEncrypt import *
from src.modules.message.cryptage.stéga_texte import *
from src.modules.message.cryptage.decalageGaucheDecrypt import *
from src.modules.message.cryptage.decalageDroiteEncrypt import *
from src.modules.message.cryptage.DecalageDroiteDecrypt import *
from flask import session


# from src.modules.message.cryptage.décalageDroitDecrypte import *


blueprint = Blueprint("message", __name__, url_prefix="/api")

class MessageAPI(BaseAPI):
    route_base = 'messages'
    model = Message
    schema = MessageSchema

    def post(self):
        # message=CryptageGauche(request.json['content'],3)
        # message=cryptage_Miroire(request.json['content'])
        #ajout decalage gauche +droit
        if request.json['type_cryptage']=="Mirroire":
            message=cryptage_Miroire(request.json['content'])
        if  request.json['type_cryptage']=="gauche":
            # message=CryptageGauche(request.json['content'],3)
            message=decalageGaucheEncrypt(request.json['content'],request.json['para1'])
            print()
        if request.json['type_cryptage']=="droite":
        #     message=decal(request.json['content'],3)
              message=decalageDroiteEncrypt(request.json['content'],request.json['para1'])
        if request.json['type_cryptage']=="Cesare":
            message=encryptTextKey(request.json['content'],request.json['para1'])
        if request.json['type_cryptage']=="Affine":
            message=crypt(request.json['content'],request.json['para1'],request.json['para2'])
        if request.json['type_cryptage']=="steganographie":
            message=stenographyCryptage(request.json['content'])
        

        verify=User.query.all()
        for v in verify:
            if v.username.lower()==request.json['sent_to'].lower():
                message=Message(owner=request.json['owner'],sent_to=request.json['sent_to'],content=message )
                db.session.add(message)
                db.session.commit()
                print("ajouté")
                return {'id':message.id}    
            
        print ("l'utilisateur n'existe pas")
        return{}

    
    
    def GetbyUsername (self,owner):
        messages_list=Message.query.all()
        messages_list2=[]
        serializer = self.schema(many=True)

        for message in messages_list:
            if (message.sent_to.lower() == owner.lower()):
                messages_list2.append(message)
        return jsonify( serializer.dump(messages_list2))
    
    def DecryptMessage(self,id):
        message = Message.query.get_or_404(id)
        serializer = self.schema()

        message.content=ChooseMethod(message.content)


        return jsonify(serializer.dump(message))


MessageAPI.register(blueprint)

def ChooseMethod(message):
    i = len(message)-1
    while message[i] not in ('m','a','g','d','c','A','S'):
        i=i-1
    method = message[i] 
    print(type(message))
    i=i+1
    dec = message[i:len(message)]	
    message = message[0:i-1] 	
    if method =='m':
        # position=Position_Mot_pal(dec)
        clair=decryptage_miroire(message,dec)
    if method =='c':
        #à modifer
        # print (dec)
        # print(type(dec))
        # clair=""
        clair=decryptTextKey(message,int(dec))
        print(type(clair))
    if method =='A':
        clair=decrypt(message,dec)
    if method=='S':
        
        clair=stenographyDecryptage(message)
    #ajout decalage gauche +droit
    if method=='g':
        message=message+method+dec
        clair=decalageGaucheDecrypt(message)
    if method=='d':
        message=message+method+dec
        clair=decalageDroiteDecrypt(message)
    return clair




