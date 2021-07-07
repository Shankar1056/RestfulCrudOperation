from Crud.config import api, app
from Crud import views

api.add_resource(views.Signup, '/signup')
api.add_resource(views.Login, '/login')
api.add_resource(views.Logout, '/logout')
api.add_resource(views.Update, '/update')
api.add_resource(views.Delete, '/delete')
api.add_resource(views.GetAllUsers, '/get_all_users')


if __name__ == '__main__':
    app.run(debug=True, port=5001)

