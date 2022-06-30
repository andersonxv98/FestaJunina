from DAO.LoginDAO import LoginDAO
from DAO.conexao import Conexao
from View.failLogin import FailLogin
from View.loginView import LoginView
from View.mainWindow import MainWindow


class ControllerLogin():
    def __init__(self):
        super(ControllerLogin, self).__init__()
        self.loginView = LoginView()
        self.loginView.show()
        self.conection = Conexao()

        self.loginView.button.clicked.connect(self.Logar)

        self.idUsuario = None
    def Logar(self):
        user = self.loginView.campo_usuario.text()
        senha = self.loginView.campo_senha.text()

        loginDao = LoginDAO(senha, user,self.conection)

        result = loginDao.Login()
        #print("RESULT: ", result)
        try:
            if result[0]:

                self.idUsuario = result[1]
                #print("ID USUARIO> ", self.idUsuario)
                self.window = MainWindow(self.idUsuario)
                #print("instanciou window")
                self.loginView.close()
                self.window.showMaximized()
                #print("max window")
        except:
            self.loginView.close()
            self.loginfail = FailLogin()
            self.loginfail.show()
            self.loginfail.disconnect()


