# PracticaSI
 Mark y Pablo

#utiles
fechas = []
    for fecha in (user[list(user.keys())[0]])['fechas']:
        fechas.append(fecha)
    ips = []
    for ip in (user[list(user.keys())[0]])['ips']:
        ips.append(ip)

print((f"INSERT INTO users VALUES('{list(user.keys())[0]}',"
                f"'{(user[list(user.keys())[0]])['contrasena']}',"
                f"{(user[list(user.keys())[0]])['permisos']}, {((user[list(user.keys())[0]])['emails'])['total']},"
                f"{((user[list(user.keys())[0]])['emails'])['phishing']}, {((user[list(user.keys())[0]])['emails'])['cliclados']},"
                f"{len((user[list(user.keys())[0]])['fechas'])}, {len((user[list(user.keys())[0]])['ips'])})"))