from flask import request
from flask_login import login_user
from flask_restful import Resource
from werkzeug.security import check_password_hash

from Crud.models import Users
from Crud.hardcodedata import LoginMessages


class Login(Resource):
    def post(self):
        data = request.get_json()

        password = data['password']
        email = data['email']

        userEmail = Users.query.filter_by(email=email).first()

        if not userEmail:
            return {'message': LoginMessages.no_user}

        userPassword = Users.query.filter_by(password=password).first()

        if not userPassword:
            return {'message': LoginMessages.check_password}
        else:
            return {'message': LoginMessages.success}
