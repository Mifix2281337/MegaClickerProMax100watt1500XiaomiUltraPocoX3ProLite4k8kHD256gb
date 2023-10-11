# Присоединить в main.py
# Импорты
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
from playsound import playsound
from PIL import Image
from PyQt5 import QtTest
import time
import random


class Boss(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("untitled1.ui", self)
        self.setWindowTitle("МОЛИСЬ")
        self.setWindowIcon(QIcon("macboss\\1.png"))
        self.btn.clicked.connect(self.clickedCheck)
        self.hp_indicator = "▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮"
        self.clicks_count = 700
        self.lbll2 = QLabel(self)
        self.lbll2.setGeometry(150, 150, 200, 200)
        image = Image.open("macboss\\1.png")
        new_image = image.resize((200, 200))
        new_image.save('new_image.png')
        self.lbll2.setPixmap(QPixmap("new_image.png"))
        self.lbll2.move(200, 30)

    # попадание
    def clickedCheck(self):
        self.clicks_count += 1
        self.clck.setText(str(self.clicks_count))
        playsound("sound\\udar2.mp3", False)
        QtTest.QTest.qWait(50)
        self.lbll2.move(200, 30)
        QtTest.QTest.qWait(50)
        self.lbll2.move(200, 40)
        QtTest.QTest.qWait(50)
        self.lbll2.move(200, 50)
        QtTest.QTest.qWait(50)
        self.lbll2.move(200, 60)
        QtTest.QTest.qWait(50)
        self.lbll2.move(200, 70)
        self.btn.move(random.randint(20, 480),random.randint(290, 480))
        if self.clicks_count == 850:
            exit()


    # регистратор промаха
    def mousePressEvent(self, event):
        self.hp_indicator = self.hp_indicator[1::]
        self.hp.setText(self.hp_indicator)
        image = Image.open("macboss\\2.png")
        new_image = image.resize((200, 200))
        new_image.save('new_image.png')
        self.lbll2.setPixmap(QPixmap("new_image.png"))
        playsound("sound\\udar.mp3", False)

        self.kick = QLabel(self)
        self.kick.setGeometry(590,690,590,690)
        self.kick.setStyleSheet("background-color: rgba(255,0,0,100)")
        self.kick.move(0,0)
        self.kick.show()
        QtTest.QTest.qWait(100)
        
        image = Image.open("macboss\\1.png")
        new_image = image.resize((200, 200))
        QtTest.QTest.qWait(50)
        self.lbll2.move(200, 50)
        QtTest.QTest.qWait(50)
        self.lbll2.move(200, 40)
        QtTest.QTest.qWait(50)
        self.lbll2.move(200, 30)
        QtTest.QTest.qWait(50)
        self.lbll2.move(200, 20)
        QtTest.QTest.qWait(50)
        self.lbll2.move(200, 10)
        QtTest.QTest.qWait(50)
        self.lbll2.move(200, 1)
        self.kick.hide()
        new_image.save('new_image.png')
        self.lbll2.setPixmap(QPixmap("new_image.png"))
        if len(self.hp_indicator) == 0:
            playsound("sound\\ha.mp3")
            exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Boss()
    playsound("sound\\doom.mp3", False)
    #QtTest.QTest.qWait(7000)
    ex.show()
    sys.exit(app.exec_())
