# Присоединить в main.py
# Импорты
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
from playsound import playsound
from PIL import Image
import time
import random

class Boss(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("untitled1.ui", self)
        self.setWindowTitle("ЕШЬ МОЛИСЬ")
        self.btn.clicked.connect(self.clickedCheck)

    def clickedCheck(self):
        print("че на")
        self.btn.move(random.randint(20, 290),random.randint(480, 575))




    # Чекер координат (не политических)
    def mousePressEvent(self, event):
        x = event.pos().x()
        y = event.pos().y()
        print(f'Координаты: ({x}, {y})')





if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Boss()
    ex.show()
    sys.exit(app.exec_())