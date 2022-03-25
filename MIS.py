import matplotlib.pyplot as plt

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
    print("\nEJERCICIO 2:\n")
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

    print("\nEJERCICIO 3:\n")
    dfPermisos0 = dfUsers[dfUsers["permisos"] == 0]
    dfPermisos1 = dfUsers[dfUsers["permisos"] == 1]
    dfEmailsMas = dfUsers[dfUsers["totalEmails"] >= 200]
    dfEmailsMenos = dfUsers[dfUsers["totalEmails"] < 200]
    print("\nEmails Totales:\n")
    print("Emails totales de phising de usuarios con permiso 0: " + str(dfPermisos0['phisingEmails'].sum()))
    print("Emails totales de phising de usuarios con permiso 1: " + str(dfPermisos1['phisingEmails'].sum()))
    print("Emails totales de phising de usuarios con 200 emails o más: " + str(dfEmailsMas['phisingEmails'].sum()))
    print("Emails totales de phising de usuarios con menos de 200 emails: " + str(dfEmailsMenos['phisingEmails'].sum()))
    print("\nMedias:\n")
    print("Media de  emails dephising de usuarios con permiso 0: " + str(dfPermisos0['phisingEmails'].mean()))
    print("Media de emails de phising de usuarios con permiso 1: " + str(dfPermisos1['phisingEmails'].mean()))
    print("Media de emails de phising de usuarios con 200 emails o más: " + str(dfEmailsMas['phisingEmails'].mean()))
    print("Media de emails de phising de usuarios con menos de 200 emails: " + str(dfEmailsMenos['phisingEmails'].mean()))
    print("\nMedianas:\n")
    print("Mediana de emails de phising de usuarios con permiso 0: " + str(dfPermisos0['phisingEmails'].median()))
    print("Mediana de emails de phising de usuarios con permiso 1: " + str(dfPermisos1['phisingEmails'].median()))
    print("Mediana de emails de phising de usuarios con 200 emails o más: " + str(dfEmailsMas['phisingEmails'].median()))
    print("Mediana de emails de phising de usuarios con menos de 200 emails: " + str(dfEmailsMenos['phisingEmails'].median()))
    print("\nVarianzas:\n")
    print("Varianza de emails de phising de usuarios con permiso 0: " + str(dfPermisos0['phisingEmails'].var()))
    print("Varianza de emails de phising de usuarios con permiso 1: " + str(dfPermisos1['phisingEmails'].var()))
    print("Varianza de emails de phising de usuarios con 200 emails o más: " + str(dfEmailsMas['phisingEmails'].var()))
    print("Varianza de emails de phising de usuarios con menos de 200 emails: " + str(dfEmailsMenos['phisingEmails'].var()))
    print("\nMáximos:\n")
    print("Máximo de emails de phising de usuarios con permiso 0: " + str(dfPermisos0['phisingEmails'].max()))
    print("Máximo de emails de phising de usuarios con permiso 1: " + str(dfPermisos1['phisingEmails'].max()))
    print("Máximo de emails de phising de usuarios con 200 emails o más: " + str(dfEmailsMas['phisingEmails'].max()))
    print("Máximo de emails de phising de usuarios con menos de 200 emails: " + str(dfEmailsMenos['phisingEmails'].max()))
    print("\nMínimos:\n")
    print("Mínimo de emails de phising de usuarios con permiso 0: " + str(dfPermisos0['phisingEmails'].min()))
    print("Mínimo de emails de phising de usuarios con permiso 1: " + str(dfPermisos1['phisingEmails'].min()))
    print("Mínimo de emails de phising de usuarios con 200 emails o más: " + str(dfEmailsMas['phisingEmails'].min()))
    print("Mínimo de emails de phising de usuarios con menos de 200 emails: " + str(dfEmailsMenos['phisingEmails'].min()))
    print("\nEJERCICIO 4:\n")
    webDesactualizadas = []
    dfDesactualizados = dfLegal.copy()
    dfDesactualizados['desact'] = dfLegal.loc[:, ['cookies','aviso','proteccionDeDatos']].sum(axis=1)
    ejex = []
    ejey = []
    while len(webDesactualizadas) < 5:
        max = dfDesactualizados['desact'].max()
        dfAux = dfDesactualizados[dfDesactualizados['desact'] == max]
        dfAux = dfAux.sort_values('creacion')
        name = list(dfAux['name'].head(1))[0]
        ejex.append(name)
        ejey.append(max)
        webDesactualizadas.append(name)
        dfDesactualizados = dfDesactualizados.drop(dfDesactualizados[dfDesactualizados['name']==name].index)
    print("Las 5 web más desactualizadas son:",end=" ")
    for web in webDesactualizadas:
        if web == webDesactualizadas[len(webDesactualizadas)-1]:
            print(web)
        else:
            print(web, end=", ")
    parameters = {'axes.labelsize': 10,
                  'xtick.labelsize':7}
    plt.rcParams.update(parameters)
    plt.bar(ejex,ejey)
    plt.ylabel("Cantidad de políticas desactualizadas")
    plt.xlabel("Nombre de la web")
    plt.title('Las 5 webs más desactualizadas')
    plt.show()