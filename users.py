import json

from basedatos import insertarUsers


def usersToDB():
    with open("Logs/users.json") as usersjson:
        users = json.load(usersjson)
    for user in users['usuarios']:
        insertarUsers(user)
