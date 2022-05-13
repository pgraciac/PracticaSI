import json

import matplotlib.pyplot as plt
import pandas as pd
from pandas.io.json import json_normalize
from sklearn import datasets, linear_model, tree
from sklearn.ensemble import RandomForestClassifier
from subprocess import call
from sklearn.datasets import load_iris
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import graphviz  # https://graphviz.org/download/


def get_users_prob():
    with open('Logs/users_IA_clases.json') as users:
        users = users.read()

    users = json.loads(users)
    users = pd.json_normalize(users['usuarios'])
    users_train_x = pd.DataFrame()
    users_train_x['porcentaje'] = users['emails_phishing_clicados'] / users['emails_phishing_recibidos']
    users_train_x['porcentaje'] = users_train_x['porcentaje'].fillna(0)
    users_train_y = users['vulnerable']

    with open('Logs/users_IA_predecir.json') as users:
        users = users.read()

    users = json.loads(users)
    users = pd.json_normalize(users['usuarios'])
    users_test_x = pd.DataFrame()
    users_test_x['porcentaje'] = users['emails_phishing_clicados'] / users['emails_phishing_recibidos']
    users_test_x['porcentaje'] = users_test_x['porcentaje'].fillna(0)
    users_name = users['usuario'].values
    print(users_name)

    return users_train_x, users_train_y, users_test_x, users_name


def get_users_all():
    with open('Logs/users_IA_clases.json') as users:
        users = users.read()

    users = json.loads(users)
    users = pd.json_normalize(users['usuarios'])
    users_train_x = users[['emails_phishing_clicados', 'emails_phishing_recibidos']]
    users_train_y = users['vulnerable']

    with open('Logs/users_IA_predecir.json') as users:
        users = users.read()

    users = json.loads(users)
    users = pd.json_normalize(users['usuarios'])
    users_test_x = users[['emails_phishing_clicados', 'emails_phishing_recibidos']]

    users_name = users['usuario'].values
    print(users_name)

    return users_train_x, users_train_y, users_test_x, users_name


def linearRegresion():
    users_train_x, users_train_y, users_test_x, users_name = get_users_prob()
    regr = linear_model.LinearRegression()
    regr.fit(users_train_x, users_train_y)

    users_pred = regr.predict(users_test_x)
    users_res = users_pred.copy()
    for user in users_res:
        if user >= 0.5:
            users_res[np.argmax(users_res == user)] = 1
        else:
            users_res[np.argmax(users_res == user)] = 0

    print(users_res)
    plt.scatter(users_test_x, users_res)
    # plt.plot(users_test_x.values, users_pred)
    plt.xticks()
    plt.yticks()
    plt.show()
    return users_res, users_name


def decisionTree():
    users_train_x, users_train_y, users_test_x, users_name = get_users_all()

    clf_model = tree.DecisionTreeClassifier()
    clf_model.fit(users_train_x, users_train_y)
    dot_data = tree.export_graphviz(clf_model, out_file=None,
                                    feature_names=['emails clicados', 'emails totales'],
                                    class_names=['no vulnerable', 'vulnerable'],
                                    filled=True, rounded=True,
                                    special_characters=True)
    graph = graphviz.Source(dot_data)
    graph.render('decisionTree.gv', view=True).replace('\\', '/')
    return clf_model.predict(users_test_x), users_name


def randomForest():
    users_train_x, users_train_y, users_test_x, users_name = get_users_all()

    clf = RandomForestClassifier(max_depth=2, random_state=0, n_estimators=10)
    clf.fit(users_train_x, users_train_y)
    print(clf.predict(users_test_x))

    for i in range(len(clf.estimators_)):
        estimator = clf.estimators_[i]
        tree.export_graphviz(estimator,
                    out_file='tree.dot',
                    feature_names=['emails clicados', 'emails totales'],
                    class_names=['no vulnerable', 'vulnerable'],
                    rounded=True, proportion=False,
                    precision=2, filled=True)
        call(['dot', '-Tpng', 'tree.dot', '-o', 'tree' + str(i) + '.png', '-Gdpi=600'])

    return clf.predict(users_test_x), users_name
