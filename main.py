from legal import legalToDB
from users import usersToDB
from basedatos import borrarLegal, borrarUsers, getFromDB,SQLStatement

if __name__ == '__main__':
    borrarLegal()
    borrarUsers()
    legalToDB()
    usersToDB()
    dfLegal = getFromDB('legal')
    dfUsers = getFromDB('users')
    print(dfUsers)
    print(dfLegal)
    print("Muestras de usuarios: " + str(dfUsers.shape[0]))
    print("Muestras de legal: " + str(dfLegal.shape[0]))
    print("Media del total de fechas en las que se ha iniciado sesión: " + str(dfUsers["fechas"].mean()))
    print("Desviación estándar del total de fechas en las que se ha iniciado sesión: " + str(dfUsers["fechas"].std(axis=0)))
    print("Media del total de ips detectadas: " + str(dfUsers["ips"].mean()))
    print("Desviación estándar del total de ips detectadas: " + str(dfUsers["ips"].std(axis=0)))
    print("Media del total de emails recibidos: " + str(dfUsers["totalEmails"].mean()))
    print("Desviación estándar del total de emails recibidos: " + str(dfUsers["totalEmails"].std(axis=0)))
    print("Máximo del total de fechas que se ha iniciado sesión: " + str(dfUsers["fechas"].max()))
    print("Mínimo del total de fechas que se ha iniciado sesión: " + str(dfUsers["fechas"].min()))
    print("Máximo del total de emails recibidos: " + str(dfUsers["totalEmails"].max()))
    print("Mínimo del total de emails recibidos: " + str(dfUsers["totalEmails"].min()))
