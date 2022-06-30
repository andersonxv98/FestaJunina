

class ProdutosDAO:
    def __init__(self, conexao):
        super().__init__()
        self.conexao = conexao


    def getProdutosDAO(self):
        #print("entrou na função getProdutosDAO")
        query = "SELECT * FROM festajunina.produtos order by valor asc"

        mycursor = self.conexao.condb
        stmycursos = mycursor.cursor()
        #print(query)
        try:
            stmycursos.execute(query)
            #s.commit()
            myresult  = stmycursos.fetchall()
            return myresult
            # mycursor.execute(query)

        except:
            #print(query)
            return ("ERROR")