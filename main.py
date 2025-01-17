from PyQt6.QtWidgets import QApplication, QMainWindow

from win import Window

import sys


if __name__ == "__main__":
    app: QApplication = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())