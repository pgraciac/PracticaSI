import numpy as np
from flask_login import LoginManager, login_user, logout_user, login_required
from flask import Flask, render_template, request, redirect, url_for, flash
import requests as rq
import hashlib

from models.ModelUser import ModelUser

from basedatos import getFromDB
from legal import outdatedWebs
from models.entities.user import User
from users import criticUsers, usersSpam
from ia import linearRegresion, decisionTree, randomForest

app = Flask(__name__)

login_manager_app = LoginManager(app)


@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(id)


@app.route('/index/', methods=['GET'])
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/usuariosVulnerablesIA/', methods=['GET'])
@login_required
def usuariosVulnerablesIA():
    regresion, names = linearRegresion()
    decTree = decisionTree()[0]
    forest = randomForest()[0]
    print(regresion, decTree, forest)

    return render_template('usuariosVulnerablesIA.html', names=names, regresion=regresion,
                           regresionCount=np.sum(regresion), decTree=decTree, decTreeCount=np.sum(decTree),
                           forest=forest, forestCount=np.sum(forest))


@app.route('/topUsuariosCriticos/', methods=['POST'])
@login_required
def topUsuariosCriticos(usersMas=None, usersMenos=None):
    dfUsers = getFromDB('users')
    numero = request.form.get('numeroUsuarios')
    users = criticUsers(dfUsers, int(numero))[0]
    cincuentamas = request.form.get('50mas')
    cincuentamenos = request.form.get('50menos')
    if cincuentamas == 'on':
        usersMas = usersSpam('mas', dfUsers)
    if cincuentamenos == 'on':
        usersMenos = usersSpam('menos', dfUsers)
    return render_template('TopUsuariosCriticos.html', users=users, usersMas=usersMas, usersMenos=usersMenos)


@app.route('/topWebsVulnerables/', methods=['POST'])
@login_required
def topWebsVulnerables():
    dfLegal = getFromDB('legal')
    numero = request.form.get('numeroWebs')
    webs = outdatedWebs(dfLegal, int(numero))[0]
    return render_template('TopWebsVulnerables.html', webs=webs, numero=numero)


@app.route('/lastVulnerabilities/', methods=['GET', 'POST'])
def lastVulnerabilities():
    response = rq.get('https://cve.circl.lu/api/last').json()
    # response = (json.dumps(response[0]))
    vulnerabilities = []
    for resp in response:
        if len(vulnerabilities) < 10:
            vulnerabilities.append(resp['id'])
        else:
            break
    return render_template('lastVulnerabilities.html', vulnerabilities=vulnerabilities)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')

        dfUsers = (getFromDB('users'))
        password = hashlib.new('md5', password.encode())
        print(list(dfUsers[dfUsers['name'] == name]['contrasena'])[0])
        if list(dfUsers[dfUsers['name'] == name]['contrasena'])[0] == password.hexdigest():
            user = User(name, password.hexdigest())
            login_user(user)
            return redirect(url_for('index'))
        else:
            return render_template('login.html')


@app.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


def error401(error):
    return render_template('notAutorized.html')


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.register_error_handler(401, error401)
    app.run(debug=True)
