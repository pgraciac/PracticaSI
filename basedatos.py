import hashlib
import sqlite3
import pandas as pd


def getFromDB(table):
    con = sqlite3.connect('PracticaSistemas.db')
    df = pd.read_sql_query(f"SELECT * FROM {table}", con)
    con.commit()
    con.close()
    return df

def SQLStatement(consulta):
    con = sqlite3.connect('PracticaSistemas.db')
    df = pd.read_sql_query(consulta, con)
    con.commit()
    con.close()
    return df

def insertarLegal(web):
    con = sqlite3.connect('PracticaSistemas.db')
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS legal(name text primary key, cookies int, aviso int, proteccionDeDatos int, creacion int)")
    cur.execute(
        f"INSERT INTO legal VALUES('{list(web.keys())[0]}', {(web[list(web.keys())[0]])['cookies']}, {(web[list(web.keys())[0]])['aviso']},"
        f"{(web[list(web.keys())[0]])['proteccion_de_datos']},{(web[list(web.keys())[0]])['creacion']})")
    con.commit()

    con.close()


def borrarLegal():
    con = sqlite3.connect('PracticaSistemas.db')
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS legal")
    con.commit()
    con.close()


def insertarUsers(user):
    con = sqlite3.connect('PracticaSistemas.db')
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS users(name text primary key, telefono int , contrasena text, provincia text,"
        " permisos int, totalEmails int, phisingEmails int, clicadosEmails int, fechas int, ips int)")

    if (user[list(user.keys())[0]])['telefono'] != 'None':
        telefono = (user[list(user.keys())[0]])['telefono']
    else:
        telefono = 'NULL'

    if (user[list(user.keys())[0]])['provincia'] != 'None':
        provincia = (user[list(user.keys())[0]])['provincia']
    else:
        provincia = 'NULL'

    cur.execute(f"INSERT INTO users VALUES('{list(user.keys())[0]}', {telefono},"
                f"'{(user[list(user.keys())[0]])['contrasena']}', '{provincia}',"
                f"{(user[list(user.keys())[0]])['permisos']}, {((user[list(user.keys())[0]])['emails'])['total']},"
                f"{((user[list(user.keys())[0]])['emails'])['phishing']}, {((user[list(user.keys())[0]])['emails'])['cliclados']},"
                f"{len((user[list(user.keys())[0]])['fechas'])}, {len((user[list(user.keys())[0]])['ips'])})")

    cur.execute("CREATE TABLE IF NOT EXISTS fecha(fecha text,name text, foreign key(name) references users(name))")
    for fecha in (user[list(user.keys())[0]])['fechas']:
        cur.execute(f"INSERT INTO fecha VALUES('{fecha}', '{list(user.keys())[0]}')")

    cur.execute("CREATE TABLE IF NOT EXISTS ip(ip text,name text, foreign key(name) references users(name))")
    for ip in (user[list(user.keys())[0]])['ips']:
        cur.execute(f"INSERT INTO ip VALUES('{ip}', '{list(user.keys())[0]}')")

    con.commit()
    con.close()


def borrarUsers():
    con = sqlite3.connect('PracticaSistemas.db')
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS users")
    con.commit()
    con.close()


def basicStats(dfUsers, dfLegal):
    print("Muestras de usuarios: " + str(dfUsers.shape[0]))
    print("Muestras de legal: " + str(dfLegal.shape[0]))
    print("Media del total de fechas en las que se ha iniciado sesión: " + str(dfUsers["fechas"].mean()))
    print("Desviación estándar del total de fechas en las que se ha iniciado sesión: " + str(
        dfUsers["fechas"].std(axis=0)))
    print("Media del total de ips detectadas: " + str(dfUsers["ips"].mean()))
    print("Desviación estándar del total de ips detectadas: " + str(dfUsers["ips"].std(axis=0)))
    print("Media del total de emails recibidos: " + str(dfUsers["totalEmails"].mean()))
    print("Desviación estándar del total de emails recibidos: " + str(dfUsers["totalEmails"].std(axis=0)))
    print("Máximo del total de fechas que se ha iniciado sesión: " + str(dfUsers["fechas"].max()))
    print("Mínimo del total de fechas que se ha iniciado sesión: " + str(dfUsers["fechas"].min()))
    print("Máximo del total de emails recibidos: " + str(dfUsers["totalEmails"].max()))
    print("Mínimo del total de emails recibidos: " + str(dfUsers["totalEmails"].min()))


def diccionarioHasheado():
    dicti = open("realhuman_phill.txt", "r", encoding='ISO-8859-1')
    diccionario = dicti.read()
    diccionario = list(diccionario.split("\n"))
    diccionarioHash = open("diccionarioHash.txt", "w")
    for dic in diccionario:
        diccionarioHash.write(hashlib.md5(dic.encode('ISO-8859-1')).hexdigest() + "\n")
    dicti.close()
    diccionarioHash.close()

def contrasenasVulnerables(dfUsers):
    contrasenas = list(dfUsers['contrasena'])
    with open("diccionarioHash.txt", "r") as dic:
        diccionario = dic.read()
    diccionario = list(diccionario.split("\n"))
    vulnerables = []
    for contrasena in contrasenas:
        if contrasena in diccionario:
            vulnerables.append(contrasena)
    return vulnerables