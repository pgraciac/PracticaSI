from basedatos import getFromDB
from models.entities.user import User


class ModelUser():

    def login(self, user):
        allUsers = getFromDB('users')['name']
        if list(allUsers[user])[0]:
            return user
        else:
            return None

    @classmethod
    def get_by_id(self, id):
        allUsers = getFromDB('users')
        useri = allUsers[allUsers['name'] == id]
        user = User(list(useri['name'])[0], list(useri['contrasena'])[0])
        return user


