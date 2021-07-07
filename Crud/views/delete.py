from flask import request
from flask_restful import Resource
from Crud.config import db
from Crud.models import Users
from Crud.hardcodedata import LoginMessages, UpdateUser, DeleteUser


class Delete(Resource):
    def delete(self):
        data = request.get_json()

        email = data['email']

        user = Users.query.filter_by(email=email).first()

        if not user:
            return {'message': LoginMessages.no_user}

        else:
            Users.query.filter_by(email=email).delete()
            db.session.commit()
            return {'message': DeleteUser.success}
