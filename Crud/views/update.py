from flask import request
from flask_restful import Resource
from Crud.config import db
from Crud.models import Users
from Crud.hardcodedata import LoginMessages, UpdateUser


class Update(Resource):
    def put(self):
        data = request.get_json()

        name = data['name']
        email = data['email']

        user = Users.query.filter_by(email=email).first()

        if not user:
            return {'message': LoginMessages.no_user}

        else:
            user.name = name
            db.session.commit()
            return {'message': UpdateUser.success}
