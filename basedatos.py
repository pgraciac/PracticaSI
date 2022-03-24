import sqlite3
import pandas as pd


def getFromDB(table):
    con = sqlite3.connect('PracticaSistemas.db')
    df = pd.read_sql_query(f"SELECT * FROM {table}", con)
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
        " permisos int, totalEmails int, phisingEmails int, clicadosEmails int, fechas text[], ips text[])")

    if (user[list(user.keys())[0]])['telefono'] != 'None':
        telefono = (user[list(user.keys())[0]])['telefono']
    else:
        telefono = 'NULL'

    if (user[list(user.keys())[0]])['provincia'] != 'None':
        provincia = (user[list(user.keys())[0]])['provincia']
    else:
        provincia = 'NULL'
    fechas = []
    for fecha in (user[list(user.keys())[0]])['fechas']:
        fechas.append(fecha)
    ips = []
    for ip in (user[list(user.keys())[0]])['ips']:
        ips.append(ip)
    cur.execute(f"INSERT INTO users VALUES('{list(user.keys())[0]}', {telefono},"
                f"'{(user[list(user.keys())[0]])['contrasena']}', '{provincia}',"
                f"{(user[list(user.keys())[0]])['permisos']}, {((user[list(user.keys())[0]])['emails'])['total']},"
                f"{((user[list(user.keys())[0]])['emails'])['phishing']}, {((user[list(user.keys())[0]])['emails'])['cliclados']},"
                f"{fechas}, {ips})")
    cur.execute("DROP TABLE IF EXISTS fecha")
    cur.execute("DROP TABLE IF EXISTS ip")

    con.commit()
    con.close()


def borrarUsers():
    con = sqlite3.connect('PracticaSistemas.db')
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS users")
    con.commit()
    con.close()
