from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor
from PyQt6 import uic

from random import randint
import sys


class Window(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('UI.ui', self)
        # self.pushButton.clicked.connect(self._click)
        self.pushButton.clicked.connect(self.paintEvent)

    def paintEvent(self, event=None) -> None:
        qp: QPainter = QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()

    def click_even(self) -> None:
        qp: QPainter = QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()

    def draw(self, qp: QPainter) -> None:
        qp.setBrush(QColor(255, 255, 0))
        for i in range(randint(2, 14)):
            radius: int = randint(0, 200)
            qp.drawEllipse(
                randint(0, 600),
                randint(0, 450),
                radius,
                radius
            )


if __name__ == "__main__":
    app: QApplication = QApplication(sys.argv)
    window: Window = Window()
    window.show()
    sys.exit(app.exec())
