import pandas as pd
from legal import legalToDB
from users import usersToDB
from basedatos import borrarLegal, borrarUsers, getFromDB, borrarFecha
import pandas as pd

if __name__ == '__main__':
    borrarLegal()
    borrarUsers()
    borrarFecha()
    legalToDB()
    usersToDB()
    #dfLegal = getFromDB('legal')
    #dfUsers = getFromDB('users')
    #print(dfUsers)
    #print(dfLegal)

