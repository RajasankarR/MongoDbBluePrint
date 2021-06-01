from app import f_app,dblogger,models
from datetime import date
from flask import request,Response
import json


@f_app.route("/users",methods=["POST"])

def create_user():
    try:
        user=models.User(request.form['name'],request.form['lastname'])
        print('user',user.__dict__)
        #user={"name":,"lastname":}       
        x=dblogger.insert(user.__dict__)       
        return Response(response=json.dumps({"message":"user created","id":str(x)}),status=200,mimetype="application/json")

    except Exception as e:

        print(e)


