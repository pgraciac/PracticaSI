from legal import legalToDB
from users import usersToDB
<<<<<<< HEAD
from basedatos import borrarLegal, borrarUsers, getFromDB
import pandas as pd
=======
from basedatos import borrarLegal, borrarUsers
>>>>>>> parent of 8bc4e70 (Tablas perfectas + recuperar de DB)

if __name__ == '__main__':
    borrarLegal()
    borrarUsers()
    legalToDB()
    usersToDB()
