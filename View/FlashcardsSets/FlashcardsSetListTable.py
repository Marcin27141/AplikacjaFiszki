from PySide6.QtWidgets import QTableWidget, QLineEdit, QTableWidgetItem, QHeaderView, QAbstractItemView
from PySide6.QtCore import Qt
from View.ViewUtilities import set_widget_font_size

class FlashcardsSetListTable(QTableWidget):   
    def __init__(self, controller) -> None:
        super().__init__()
        self.setColumnCount(1)
        self.setHorizontalHeaderLabels(["Created sets"])
        self.controller = controller
        available_sets = controller.get_available_sets()
        self.populate_table(available_sets)
        self.itemClicked.connect(self.show_set_details)

        #self.setRowCount(len(available_sets))
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.horizontalHeader().setSectionsMovable(False)
        self.horizontalHeader().setSectionsClickable(False)


        set_widget_font_size(self, 15)
        
    def populate_table(self, flashcards_sets):
        for row, _set in enumerate(flashcards_sets):
            self.insertRow(row)
            table_widget_item = QTableWidgetItem(_set.name)
            self.setItem(row, 0, table_widget_item)
            table_widget_item.setData(self.controller.SET_ROLE, _set)

    def show_set_details(self, item):
        flashcards_set = item.data(self.controller.SET_ROLE)
        self.controller.show_set_details(flashcards_set)

    def showEvent(self, event):
        super().showEvent(event)
        self.clearContents()
        self.setRowCount(0)
        available_sets = self.controller.get_available_sets()
        self.populate_table(available_sets)

    