from flask import request
from flask_login import login_user
from flask_restful import Resource
from werkzeug.security import check_password_hash

from Crud.models import Users
from Crud.hardcodedata import LoginMessages


class GetAllUsers(Resource):
    def post(self):

        users = Users.query.all()
        allUser = []
        for uer in users:



            return {'message': LoginMessages.success}
