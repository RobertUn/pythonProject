from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QColor, QPainter

from random import randint

from des import UiWindow


class Window(UiWindow, QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self) -> None:
        self.setupUi(self)
        self.push_button.clicked.connect(self.paintEvent)

    def paintEvent(self, event=None) -> None:
        qp: QPainter = QPainter()
        qp.begin(self)
        self.draw_obj(qp)
        qp.end()

    def draw_obj(self, qp: QPainter) -> None:
        qp.setBrush(QColor(
            randint(0, 255),
            randint(0, 255),
            randint(0, 255)
        ))
        for i in range(randint(2, 14)):
            radius: int = randint(0, 200)
            qp.drawEllipse(
                randint(0, 600),
                randint(0, 450),
                radius,
                radius
            )