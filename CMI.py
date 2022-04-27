from flask import Flask, render_template, request

from basedatos import getFromDB
from legal import outdatedWebs
from users import criticUsers, usersSpam

app = Flask(__name__)

@app.route('/index/')
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/topUsuariosCriticos/', methods = ['POST'])
def topUsuariosCriticos(usersMas = None, usersMenos = None):
    dfUsers = getFromDB('users')
    numero = request.form.get('numeroUsuarios')
    users = criticUsers(dfUsers,int(numero))[0]
    cincuentamas = request.form.get('50mas')
    cincuentamenos = request.form.get('50menos')
    if cincuentamas == 'on':
        usersMas = usersSpam('mas', dfUsers)
    if cincuentamenos == 'on':
        usersMenos = usersSpam('menos', dfUsers)
    return render_template('TopUsuariosCriticos.html', users = users, usersMas = usersMas, usersMenos = usersMenos)

@app.route('/topWebsVulnerables/', methods = ['POST'])
def topWebsVulnerables():
    dfLegal = getFromDB('legal')
    numero = request.form.get('numeroWebs')
    webs = outdatedWebs(dfLegal, int(numero))[0]
    return render_template('TopWebsVulnerables.html', webs=webs, numero=numero)

if __name__ == '__main__':
    app.run(debug=True)