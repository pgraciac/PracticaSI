import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import json

with open("Logs/users_IA_clases.json") as usersjson:
    users = json.load(usersjson).get('usuarios')
print(users)
usuarios_train_x = []
usuarios_train_y = []
for user in users:
    if user.get('emails_phishing_clicados') != 0:
        usuarios_train_x.append(user.get('emails_phishing_clicados') / user.get('emails_phishing_recibidos'))
    else:
        usuarios_train_x.append(0)
    usuarios_train_y.append(user.get('vulnerable'))
print(usuarios_train_x, usuarios_train_y)

with open("Logs/users_IA_predecir.json") as usersjson:
    users = json.load(usersjson).get('usuarios')
print(users)
usuarios_predecir_x = []
for user in users:
    if user.get('emails_phishing_clicados') != 0:
        usuarios_predecir_x.append(user.get('emails_phishing_clicados') / user.get('emails_phishing_recibidos'))
    else:
        usuarios_predecir_x.append(0)


def linearRegresion():
    regr = linear_model.LinearRegression()
    regr.fit(usuarios_train_x, usuarios_train_y)
    users_pred = regr.predict(usuarios_predecir_x)
    print(users_pred)


linearRegresion()
