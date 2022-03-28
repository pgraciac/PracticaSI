import json
import matplotlib.pyplot as plt

from basedatos import insertarUsers


def usersToDB():
    with open("Logs/users.json") as usersjson:
        users = json.load(usersjson)
    for user in users['usuarios']:
        insertarUsers(user)


def showCritcUsers(dfUsers):
    vulnerables = ['5f4dcc3b5aa765d61d8327deb882cf99', '3bf1114a986ba87ed28fc1b5884fc2f8',
                   '276f8db0b86edaa7fc805516c852c889', '84d961568a65073a3bcf0eb216b2a576',
                   '0acf4539a14b3aa27deeb4cbdf6e989f', '1660fe5c81c4ce64a2611494c439e1ba',
                   'd16d377af76c99d27093abc22244b342', 'eb0a191797624dd3a48fa681d3061212',
                   '714ab9fbdad5c5da1b5d34fe1a093b79', 'd8578edf8458ce06fbc5bb76a58c5ca4',
                   '4297f44b13955235245b2497399d7a93', '37b4e2d82900d5e94b8da524fbeb33c0',
                   'd0763edaa9d9bd2a9516280e9044d885', 'a152e841783914146e4bcd4f39100686']
    usersVulnerable = []
    usersVulnerableCriticidad = []
    dfUsersCriticos = dfUsers.copy()
    dfUsersCriticos['criticidad'] = dfUsersCriticos['clicadosEmails'] / dfUsersCriticos['phisingEmails']
    dfUsersCriticos = dfUsersCriticos.sort_values("criticidad", ascending=False)
    for i in dfUsersCriticos.index:
        if dfUsersCriticos['contrasena'][i] in vulnerables and len(usersVulnerable) <= 10:
            usersVulnerable.append(dfUsersCriticos['name'][i])
            usersVulnerableCriticidad.append(dfUsersCriticos['criticidad'][i])
    parameters = {'axes.labelsize': 10,
                  'xtick.labelsize': 6}
    plt.rcParams.update(parameters)
    plt.xticks(rotation=32)
    plt.bar(usersVulnerable, usersVulnerableCriticidad, color='red')
    plt.ylabel("Criticidad")
    plt.xlabel("Usuarios")
    plt.title('Los 10 usuarios más críticos')
    plt.show()


def showComparativeUsers(dfUsers):
    vulnerables = ['5f4dcc3b5aa765d61d8327deb882cf99', '3bf1114a986ba87ed28fc1b5884fc2f8',
                   '276f8db0b86edaa7fc805516c852c889', '84d961568a65073a3bcf0eb216b2a576',
                   '0acf4539a14b3aa27deeb4cbdf6e989f', '1660fe5c81c4ce64a2611494c439e1ba',
                   'd16d377af76c99d27093abc22244b342', 'eb0a191797624dd3a48fa681d3061212',
                   '714ab9fbdad5c5da1b5d34fe1a093b79', 'd8578edf8458ce06fbc5bb76a58c5ca4',
                   '4297f44b13955235245b2497399d7a93', '37b4e2d82900d5e94b8da524fbeb33c0',
                   'd0763edaa9d9bd2a9516280e9044d885', 'a152e841783914146e4bcd4f39100686']
    mediaVulnera = 0
    mediaNoVulnera = 0
    for i in dfUsers.index:
        if dfUsers['contrasena'][i] in vulnerables:
            mediaVulnera += dfUsers['fechas'][i]
        else:
            mediaNoVulnera += dfUsers['fechas'][i]
    mediaVulnera /= len(vulnerables)
    mediaNoVulnera /= (dfUsers.shape[0] - len(vulnerables))
    plt.bar(["Usuarios Vulnerables", "Usuarios No Vulnerables"], [mediaVulnera, mediaNoVulnera],
            color=['blue', 'orange'])
    plt.title("Comparativa")
    plt.text(0, mediaVulnera, mediaVulnera, ha='center')
    plt.text(1, mediaNoVulnera, mediaNoVulnera, ha='center')
    plt.show()


def showComparativePassword(dfUsers):
    vulnerables = ['5f4dcc3b5aa765d61d8327deb882cf99', '3bf1114a986ba87ed28fc1b5884fc2f8',
                   '276f8db0b86edaa7fc805516c852c889', '84d961568a65073a3bcf0eb216b2a576',
                   '0acf4539a14b3aa27deeb4cbdf6e989f', '1660fe5c81c4ce64a2611494c439e1ba',
                   'd16d377af76c99d27093abc22244b342', 'eb0a191797624dd3a48fa681d3061212',
                   '714ab9fbdad5c5da1b5d34fe1a093b79', 'd8578edf8458ce06fbc5bb76a58c5ca4',
                   '4297f44b13955235245b2497399d7a93', '37b4e2d82900d5e94b8da524fbeb33c0',
                   'd0763edaa9d9bd2a9516280e9044d885', 'a152e841783914146e4bcd4f39100686']
    plt.bar(["Comprometidas", "No Comprometidas"], [len(vulnerables), (dfUsers.shape[0] - len(vulnerables))],
            color=['red', 'green'])
    plt.title("Contraseñas Comprometidas vs No Comprometidas")
    plt.show()
