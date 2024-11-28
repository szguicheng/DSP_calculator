import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(300, 400, 1600, 2400)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('resources/DSP.png'))        

        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('resources/DSP.png'))
    ex = Example()
    sys.exit(app.exec_())