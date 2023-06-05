from PySide6.QtWidgets import QTableWidget, QStyledItemDelegate, QTableWidgetItem, QHeaderView, QAbstractItemView, QMessageBox
from PySide6.QtCore import Qt, QTimer
from datetime import datetime
from View.ViewUtilities import set_widget_font_size


class NonEditableDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        return None

    def editorEvent(self, event, model, option, index):
        return False

class FlashcardSetStatsTable(QTableWidget):   
    COLUMNS_COUNT = 4
    
    def __init__(self) -> None:
        super().__init__()
        self.setColumnCount(self.COLUMNS_COUNT)
        self.setHorizontalHeaderLabels(["Original", "Translation", "Accuracy", "Last tested"])
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setRowCount(1)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.horizontalHeader().setSectionsClickable(False)
        self.horizontalHeader().setSectionsMovable(False)
        set_widget_font_size(self, 15)

    def load_set_for_viewing(self, flashcards_set):
        self.clearContents()
        self.setRowCount(len(flashcards_set.flashcards))
        for row, flashcard in enumerate(flashcards_set.flashcards):
            original = QTableWidgetItem(flashcard.original)
            translation = QTableWidgetItem(flashcard.translation)
            all_answers = flashcard.times_correct + flashcard.times_incorrect
            accuracy = '-' if all_answers == 0 else f"{round(flashcard.times_correct / all_answers, 2) * 100}%"
            accuracy = QTableWidgetItem(accuracy)
            last_tested = str(datetime.strptime(flashcard.last_tested, r"%Y-%m-%d %H:%M:%S.%f").date()) if flashcard.last_tested else '-'
            last_tested = QTableWidgetItem(last_tested)
            self.setItem(row, 0, original)
            self.setItem(row, 1, translation)
            self.setItem(row, 2, accuracy)
            self.setItem(row, 3, last_tested)
            