# Присоединить в main.py
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from playsound import playsound
from PIL import Image
import time

class Boss(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("untitled1.ui", self)
        self.setWindowTitle("ЕШЬ МОЛИСЬ БУХАЙ ЕБИСЬ")






if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Boss()
    ex.show()
    sys.exit(app.exec_())