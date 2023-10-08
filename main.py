import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from playsound import playsound
from PIL import Image
import time


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("untitled.ui", self)
        self.setWindowTitle("Кликер")
        self.btn2.clicked.connect(self.button)
        self.setWindowIcon(QIcon("photo\\nice.png"))
        self.lbll = QLabel(self)
        self.lbll.setGeometry(150, 150, 200, 200)
        self.lbll.move(110, 1)
        self.count = 0
        self.level = 1

    def button(self):
        playsound("sound\\click.mp3", False)
        self.count += 1
        self.label.setText(str(self.count))
        
        if self.count == 10:
            self.level += 1
            self.label2.setText(str(self.level))
            image = Image.open("photo\\Sena.jpg")
            new_image = image.resize((200, 200))  # сжимаем изображение
            new_image.save('new_image.jpg')
            self.lbll.setPixmap(QPixmap("new_image.jpg"))
            self.lbll.move(110, 1)
            playsound("sound\\win.mp3", False)
        
        elif self.count == 50:
            image = Image.open("photo\\Gala.jpg")
            new_image = image.resize((200, 200))  # сжимаем изображение
            new_image.save('new_image.jpg')
            self.lbll.setPixmap(QPixmap('new_image.jpg'))
            self.lbll.move(110, 1)
            playsound("sound\\gala.mp3", False)
            playsound("sound\\win.mp3", False)
        
        elif self.count == 100:
            image = Image.open("photo\\babuska.jpg")
            new_image = image.resize((200, 200))  # сжимаем изображение
            new_image.save('new_image.jpg')
            self.lbll.setPixmap(QPixmap('new_image.jpg'))
            self.lbll.move(150, 1)
            playsound("sound\\win.mp3", False)
            playsound("sound\\baba.mp3", False)
        
        elif self.count == 150:
            image = Image.open("photo\\pirat.jpg")
            new_image = image.resize((200, 200))  # сжимаем изображение
            new_image.save('new_image.jpg')
            self.lbll.setPixmap(QPixmap('new_image.jpg'))
            self.lbll.move(150, 1)
            playsound("sound\\win.mp3", False)
            playsound("sound\\palundra.mp3", False)
        
        elif self.count == 200:
            self.level += 1
            self.label2.setText(str(self.level))
            image = Image.open("photo\\sleep.jpg")
            new_image = image.resize((200, 200))  # сжимаем изображение
            new_image.save('new_image.jpg')
            self.lbll.setPixmap(QPixmap('new_image.jpg'))
            self.lbll.move(150, 1)
            playsound("sound\\win.mp3", False)
            playsound("sound\\spit.mp3", False)
        
        elif self.count == 300:
            image = Image.open("photo\\Serega.jpg")
            new_image = image.resize((200, 200))  # сжимаем изображение
            new_image.save('new_image.jpg')
            self.lbll.setPixmap(QPixmap('new_image.jpg'))
            self.lbll.move(150, 1)
            playsound("sound\\win.mp3", False)
            playsound("sound\\zashel.mp3", False)
        
        elif self.count == 400:
            image = Image.open("photo\\danil.jpg")
            new_image = image.resize((200, 200))  # сжимаем изображение
            new_image.save('new_image.jpg')
            self.lbll.setPixmap(QPixmap('new_image.jpg'))
            self.lbll.move(150, 1)
            playsound("sound\\win.mp3", False)
            playsound("sound\\mir.mp3", False)
        
        elif self.count == 500:
            self.level += 1
            self.lbll.setText(str(self.level))
            self.lbll.setText(" ")
            playsound("sound\\ha.mp3", True)
            playsound("sound\\1.mp3", False)
            image = Image.open("photo\\makar.jpg")
            new_image = image.resize((200, 200))  # сжимаем изображение
            new_image.save('new_image.jpg')
            self.lbll.setPixmap(QPixmap("new_image.jpg"))
            self.lbll.move(150, 1)
            playsound("sound\\MK.mp3", False)
        
        elif self.count == 700:
            playsound("sound\\fatality.mp3", block=False)
            self.lbll.setText("Ты победил. Красавчик.")
            self.lbll.setGeometry(150, 150, 200, 200)
            self.lbll.move(150, 1)
            time.sleep(3)
            exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())