import sys

from PyQt6.QtWidgets import QApplication


from Controllers.controllerLogin import ControllerLogin

from View.mainWindow import MainWindow


app = QApplication(sys.argv)


controlLogin = ControllerLogin()




#window.show()

app.exec()
