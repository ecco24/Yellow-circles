import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
from random import randint


class Machine(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()

    def initUI(self):
        self.do_paint = False
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Git и жёлтые окружноси')
        self.Btn.resize(120, 25)
        self.Btn.move(140, 5)
        self.Btn.clicked.connect(self.creating)

    def creating(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.drawing(qp)
            qp.end()

    def drawing(self, qp):
        side = randint(1, 300)
        begin = (400 - side) // 2
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(begin, begin, side, side)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Machine()
    ex.show()
    sys.exit(app.exec())