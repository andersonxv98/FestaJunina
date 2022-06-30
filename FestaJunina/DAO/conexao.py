import mysql.connector


class Conexao:
    def __init__(self):
        super().__init__()

        self.condb = self.Con()

    def Con(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="festajunina"
            )
            #print(mydb)

            #print("SUCESSO")
            return mydb

        except:

            return "Não conectado"