from PyQt6 import QtCore, QtWidgets


class UiWindow(object):
    def setupUi(self, window):
        window.setObjectName("MainWindow")
        window.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(window)
        self.centralwidget.setObjectName("centralwidget")
        self.table = QtWidgets.QTableView(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(10, 30, 780, 560))
        self.table.setObjectName("table")
        window.setCentralWidget(self.centralwidget)

        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("MainWindow", "Espresso"))