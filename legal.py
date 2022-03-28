import json
import matplotlib.pyplot as plt
from basedatos import insertarLegal

def legalToDB():
    with open("Logs/legal.json") as legaljson:
        legal = json.load(legaljson)
    for web in legal['legal']:
        insertarLegal(web)


def showOutdatedWebs(dfLegal):
    webDesactualizadas = []
    dfDesactualizados = dfLegal.copy()
    dfDesactualizados['desact'] = dfLegal.loc[:, ['cookies', 'aviso', 'proteccionDeDatos']].sum(axis=1)
    ejex = []
    ejey = []
    while len(webDesactualizadas) < 5:
        min = dfDesactualizados['desact'].min()
        dfAux = dfDesactualizados[dfDesactualizados['desact'] == min]
        dfAux = dfAux.sort_values('creacion')
        name = list(dfAux['name'].head(1))[0]
        ejex.append(name)
        ejey.append(min)
        webDesactualizadas.append(name)
        dfDesactualizados = dfDesactualizados.drop(dfDesactualizados[dfDesactualizados['name'] == name].index)
    plt.bar(ejex, ejey, color='blue')
    plt.ylabel("Cantidad de políticas desactualizadas")
    plt.xlabel("Nombre de la web")
    plt.title('Las 5 webs más desactualizadas')
    plt.show()


def showPrivacyPoliticy(dfLegal):
    anos = sorted(dfLegal['creacion'].unique().tolist())
    siPoli = [0] * len(anos)
    noPoli = [0] * len(anos)
    i = 0
    for ano in anos:
        dfAux = dfLegal[dfLegal['creacion'] == ano]['proteccionDeDatos']
        for aux in list(dfAux):
            if aux == 0:
                noPoli[i] += 1
            else:
                siPoli[i] += 1
        i += 1
    ancho = 0.4
    plt.bar(anos, siPoli, ancho, label='Tiene política')
    anosb = anos.copy()
    for i in range(len(anosb)):
        anosb[i] += ancho
    plt.bar(anosb, noPoli, ancho, label='No tiene política')
    plt.legend(loc='best')
    plt.title("Número de páginas web con política de privacidad frente a las que no por año")
    plt.show()