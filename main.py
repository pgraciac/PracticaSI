from legal import legalToDB
from users import usersToDB
from basedatos import borrarLegal, borrarUsers

if __name__ == '__main__':
    borrarLegal()
    borrarUsers()
    legalToDB()
    usersToDB()
