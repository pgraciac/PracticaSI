from legal import legalToDB, showOutdatedWebs, showPrivacyPoliticy
from users import usersToDB, showCritcUsers, showComparativeUsers, showComparativePassword
from basedatos import borrarLegal, borrarUsers, getFromDB, statsByGroups, basicStats
import hashlib

if __name__ == '__main__':
    borrarLegal()
    borrarUsers()
    legalToDB()
    usersToDB()
    dfLegal = getFromDB('legal')
    dfUsers = getFromDB('users')
    print("\nEJERCICIO 2:\n")
    basicStats(dfUsers,dfLegal)

    print("\nEJERCICIO 3:\n")
    statsByGroups(dfUsers, dfLegal)

    print("\nEJERCICIO 4:\n")
    print("Gráficas: \n")
    showCritcUsers(dfUsers)
    showOutdatedWebs(dfLegal)
    showComparativeUsers(dfUsers)
    showPrivacyPoliticy(dfLegal)
    showComparativePassword(dfUsers)
