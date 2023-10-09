from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Установка названия окна
        self.setWindowTitle('Мое окно')

        # Установка размеров окна
        self.setGeometry(100, 100, 800, 600)

        # Установка иконки окна
        #self.setWindowIcon(QIcon('icon.png'))

        # Создание лейбла
        self.label = QLabel('Привет, мир!', self)
        self.label.move(50, 50)

if __name__ == '__main__':
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec_()
