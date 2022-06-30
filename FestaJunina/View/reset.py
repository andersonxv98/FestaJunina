from PyQt6.QtWidgets import QPushButton


class ResetBtn(QPushButton):
    def __init__(self):
        super(ResetBtn, self).__init__()
        self.setText("RESETAR")
        self.setMaximumWidth(100)