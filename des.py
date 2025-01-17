from PyQt6 import QtCore, QtWidgets


class UiWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 450)
        self.central_w = QtWidgets.QWidget(MainWindow)
        self.central_w.setObjectName("centralwidget")
        self.push_button = QtWidgets.QPushButton(self.central_w)
        self.push_button.setGeometry(QtCore.QRect(500, 400, 80, 30))
        self.push_button.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.central_w)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Git Circles"))
        self.push_button.setText(_translate("MainWindow", "Рисовать"))