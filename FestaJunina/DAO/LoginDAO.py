
class LoginDAO:
    def __init__(self,  senha,usuario, con):
        super(LoginDAO, self).__init__()
        self.conexao = con
        self.usuario = usuario
        self.senha= senha
    def Login(self):
        try:
            #print("VALOR USUARIO: ", self.usuario, "VALOR SENHA: ", self.senha)
            query = "SELECT id FROM usuario WHERE usuario =  "+"'"+str(self.usuario)+"'"+"   and senha = "+"'"+str(self.senha)+"'"+""
            #print("Entrou na função login da classe PDO CONTROLLER")
            mycursor = self.conexao.condb
            stmycursos = mycursor.cursor()

            stmycursos.execute(query)

            myresult = stmycursos.fetchall()
            #print("REULT LOGIN DAO:", myresult)
            #for x in myresult:
                #print("resultado da busca do db: ", x)
            mycursor.close()
            return True, myresult[0][0]
        except:
            #print("IMPOSSIVEL LOGAR, VERIFIQUE O NOME DE USUARIO E A SENHA E TENTE NOVAMENTE")
            return False
