

class Venda_ProdutoDAO:
    def __init__(self, conexao):
        super().__init__()
        self.conexao = conexao

    def InsertVenda_ProdutosDAO(self, id_venda, id_produto):
        #print("EBNTRUO NA INSERVENTA_PRODDAO ----------------------------------------------------------")
        #print("entrou na função insertVendaDAO")
        mycursor = self.conexao.condb
        stmycursos = mycursor.cursor()
        sql = "INSERT INTO venda_produtos (`fk_id_venda`, `fk_id_produtos`) VALUES (%s, %s)"
        val = (str(id_venda), str(id_produto))
        #print(sql)
        try:
            stmycursos.execute(sql, val)
            mycursor.commit()
            #print("EXECUTADO COM SUCESSO")
        except:
            #print("ERRO DB")
            return ("ERROR")
    def getQuantItensVendidos(self, id_produto):
        try:
            #print("ID DO PRODUTO DENTRO GETDAO: ", id_produto)
            query = "SELECT count(fk_id_produtos) FROM festajunina.venda_produtos where fk_id_produtos = "+str(id_produto)

            mycursor = self.conexao.condb
            stmycursos = mycursor.cursor()

            stmycursos.execute(query)
            #print("passou do QUERY")
            myresult = stmycursos.fetchall()
            #print("REULT LOGIN DAO:", myresult)
            # for x in myresult:
            # print("resultado da busca do db: ", x)
            #mycursor.close()
            return myresult[0][0]

        except:
            return ("ERRO COUNT PRODUTOS")