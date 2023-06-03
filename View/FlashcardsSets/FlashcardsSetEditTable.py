from PySide6.QtWidgets import QTableWidget, QLineEdit, QTableWidgetItem, QHeaderView, QAbstractItemView
from PySide6.QtCore import Qt, QTimer
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
        self.cellClicked.connect(self.edit_cell)
        set_widget_font_size(self, 15)

    def edit_cell(self, row, col):
        item = self.item(row, col)
        if item is None:
            item = QTableWidgetItem()
            self.setItem(row, col, item)
        self.setCurrentCell(row, 0)
        item.setFlags(item.flags() | Qt.ItemIsEditable)
        self.editItem(item)

    def add_row_with_edit(self, row_idx):
        self.insertRow(row_idx)
        QTimer.singleShot(0, lambda: self.edit_cell(row_idx, 0))

    def load_set_for_edit(self, flashcards_set):
        self.clearContents()
        self.setRowCount(len(flashcards_set.flashcards))
        for row, flashcard in enumerate(flashcards_set.flashcards):
            original = QTableWidgetItem(flashcard.original)
            translation = QTableWidgetItem(flashcard.translation)
            self.setItem(row, 0, original)
            self.setItem(row, 1, translation)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            current_index = self.currentIndex()
            current_row = current_index.row()
            current_column = current_index.column()
            if current_column == self.columnCount() - 1:
                self.add_row_with_edit(current_row+1)
