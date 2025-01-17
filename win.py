from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from PyQt6.QtWidgets import QMainWindow

from des import UiWindow


class Window(UiWindow, QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self) -> None:
        db: QSqlDatabase = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('coffee.sqlite')
        db.open()
        model: QSqlDatabase = QSqlTableModel(self, db)
        model.setTable('')  # TODO название главной таблицы
        model.select()
        self.table.setModel(model)
