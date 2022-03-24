import json

from basedatos import insertarLegal

def legalToDB():
    with open("Logs/legal.json") as legaljson:
        legal = json.load(legaljson)
    for web in legal['legal']:
        insertarLegal(web)