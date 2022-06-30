import datetime


class VendaDAO:
    def __init__(self, conexao):
        super().__init__()
        self.conexao = conexao


    def getVendasDAO(self):
        #print("entrou na função getProdutosDAO")
        another_query = "SET lc_time_names =  'pt_BR'"

        query = "SELECT vendas.id, total, valorpago, troco, DATE_FORMAT(data, '%d %M %Y - %H:%i:%s'), trocaficha,nome FROM vendas INNER JOIN usuario ON usuario.id = vendas.fk_id_usuario order by id desc limit 100"
        mycursor = self.conexao.condb
        stmycursos = mycursor.cursor()
        #print(query)
        try:
            stmycursos.execute(another_query)

            stmycursos.execute(query)

            myresult  = stmycursos.fetchall()
            return myresult


        except:
            return ("ERROR")
    def getLastVendaReg(self):
        #print("entrou na função getProdutosDAO")
        query = "SELECT id FROM vendas order by id  desc LIMIT 1 ;"

        mycursor = self.conexao.condb
        stmycursos = mycursor.cursor()
        #print(query)
        try:
            stmycursos.execute(query)
            # s.commit()
            myresult = stmycursos.fetchall()
            return myresult
            # mycursor.execute(query)

        except:
            return ("ERROR")

    def getLastVendaPerID(self, id_user):
        # print("entrou na função getProdutosDAO")
        query = "SELECT * FROM festajunina.vendas  where fk_id_usuario = "+str(id_user)+ "order by id desc limit 1 "

        mycursor = self.conexao.condb
        stmycursos = mycursor.cursor()
        # print(query)
        try:
            stmycursos.execute(query)
            # s.commit()
            myresult = stmycursos.fetchall()
            return myresult
            # mycursor.execute(query)

        except:
            return ("ERROR")

    def insertVendaDAO(self, valorpago, valortotal, troco,trocaficha, id_user):
        date = datetime.datetime.today()
        #print("DATE: ", date)
        #print("entrou na função insertVendaDAO")
        #query = "INSERT INTO `festajunina`.`vendas` (`data`, `total`, `trocaficha`, 'valorpago` ,'troco`) VALUES ("+str(date)+", "+str(valortotal)+", "+str(trocaficha)+","+str(valorpago)+","+str(troco)+")"


        mycursor = self.conexao.condb
        stmycursos = mycursor.cursor()

        sql = "INSERT INTO vendas (data, total, trocaficha, valorpago, troco, fk_id_usuario) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (str(date), str(valortotal), str(trocaficha), str(valorpago), str(troco), str(id_user))


        #print(sql)
        try:
            stmycursos.execute(sql, val)
            mycursor.commit()
            #print("EXECUTADO COM SUCESSO")
            id_db = self.getLastVendaReg()
            return id_db
        except:
            return ("ERROR DB")

