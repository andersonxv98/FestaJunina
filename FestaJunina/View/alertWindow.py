from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMessageBox, QDialog, QVBoxLayout, QLabel, QDialogButtonBox


class AlertWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Confirmando")

        QBtn = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        #self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        self.message = QLabel("Confirmar Venda?")
        self.layout.addWidget(self.message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

