from flask import Flask, render_template

from basedatos import getFromDB
from users import criticUsers

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<p>Hello, World!</p>'

@app.route('/ejercicio2/')
def ejercicio2():
    dfLegal = getFromDB('legal')
    dfUsers = getFromDB('users')
    users = criticUsers(dfUsers)[0]
    return render_template('ejercicio2.html', users = users)

if __name__ == '__main__':
    app.run(debug=True)