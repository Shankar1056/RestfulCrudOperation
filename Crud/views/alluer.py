from flask_restful import Resource
from Crud.models import Users
from Crud.hardcodedata import LoginMessages


class GetAllUsers(Resource):
    def get(self):

        users = Users.query.all()
        allUser = []
        for user in users:
            userData = {
                "id": user.id,
                "name" : user.name,
                "email" : user.email,
                "password" : user.password
            }

            allUser.append(Users(userData))

            return {userData}
