from PyQt6.QtWidgets import QLabel


class Mask(QLabel):
    def __init__(self):
        super(Mask, self).__init__()
        self.setText("R$ ")
