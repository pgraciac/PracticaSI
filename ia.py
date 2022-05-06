import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import json
import numpy as np

def linearRegresion():
    with open("Logs/users_IA_clases.json") as usersjson:
        users = json.load(usersjson).get('usuarios')
    usuarios_train_x = []
    usuarios_train_y = []
    usuarios = []
    for user in users:
        usuarios.append(user.get('usuario'))
        usuarios_train_x.append([user.get('emails_phishing_clicados'), user.get('emails_phishing_recibidos')])
        usuarios_train_y.append(user.get('vulnerable'))
    with open("Logs/users_IA_predecir.json") as usersjson:
        users = json.load(usersjson).get('usuarios')
    usuarios_predecir_x = []
    for user in users:
        usuarios_predecir_x.append([user.get('emails_phishing_clicados'), user.get('emails_phishing_recibidos')])

    regr = linear_model.LinearRegression()
    regr.fit(usuarios_train_x, usuarios_train_y)
    users_pred = regr.predict(usuarios_predecir_x)
    for user in users_pred:
        if user >= 0.5:
            users_pred[np.argmax(users_pred == user)] = 1
        else:
            users_pred[np.argmax(users_pred == user)] = 0
    fig = plt.figure()

    plt.scatter(usuarios_predecir_x, users_pred)
    plt.plot(usuarios_predecir_x, users_pred)
    plt.grid()


linearRegresion()
