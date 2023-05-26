from PySide6.QtWidgets import QTableWidget, QLineEdit, QTableWidgetItem, QHeaderView, QAbstractItemView
from PySide6.QtCore import Qt
from View.ViewUtilities import set_widget_font_size

class FlashcardSetEditTable(QTableWidget):   
    def __init__(self) -> None:
        super().__init__()
        self.setColumnCount(2)
        self.setHorizontalHeaderLabels(["Original", "Translation"])
        self.setRowCount(1)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.horizontalHeader().setSectionsClickable(False)
        self.horizontalHeader().setSectionsMovable(False)

        set_widget_font_size(self, 15)

    def add_row_with_edit_finish(self):
        row_count = self.rowCount()
        self.insertRow(row_count)
        #self.setCurrentCell(row_count, 0)

    def load_set_for_edit(self, flashcards_set):
        self.clear()
        self.setRowCount(len(flashcards_set.flashcards))
        for row, flashcard in enumerate(flashcards_set.flashcards):
            original = QTableWidgetItem(flashcard.original)
            translation = QTableWidgetItem(flashcard.translation)
            self.setItem(row, 0, original)
            self.setItem(row, 1, translation)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            index = self.indexAt(event.pos())
            if index.isValid():
                self.edit(index)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            current_index = self.currentIndex()
            current_row = current_index.row()
            current_column = current_index.column()

            if current_column == self.columnCount() - 1:
                self.add_row_with_edit_finish()
