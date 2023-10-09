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

        self.hp_indicator = "▮▮▮▮▮▮▮▮▮▮"
        self.clicks_count = 700

    # попадание
    def clickedCheck(self):
        self.clicks_count += 1
        self.clck.setText(str(self.clicks_count))
        self.btn.move(random.randint(20, 480),random.randint(290, 480))

    # регистратор промаха
    def mousePressEvent(self, event):
        self.hp_indicator = self.hp_indicator[1::]
        self.hp.setText(self.hp_indicator)
        if len(self.hp_indicator) == 0:
            exit()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Boss()
    ex.show()
    sys.exit(app.exec_())