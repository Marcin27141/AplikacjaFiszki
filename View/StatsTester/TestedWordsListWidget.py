from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView
from PySide6.QtGui import QColor
from View.ViewUtilities import set_widget_font_size

class TestedWordsListWidget(QTableWidget):   
    def __init__(self) -> None:
        super().__init__()
        self.setColumnCount(2)
        self.setHorizontalHeaderLabels(["Original", "Translation"])
        self.setEditTriggers(QTableWidget.NoEditTriggers)
        self.setSelectionMode(QTableWidget.NoSelection)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.horizontalHeader().setSectionsClickable(False)
        self.horizontalHeader().setSectionsMovable(False)
        set_widget_font_size(self, 15)

    def present_tested_flashcards(self, tested_flashcards):
        self.setRowCount(len(tested_flashcards))
        self.populate_list(tested_flashcards)

    def populate_list(self, tested_flashcards):
        for row, (flashcard, was_correct) in enumerate(tested_flashcards):
            original_widget = QTableWidgetItem(flashcard.original)
            translation_widget = QTableWidgetItem(flashcard.translation)
            self.set_right_color(original_widget, was_correct)
            self.set_right_color(translation_widget, was_correct)
            self.setItem(row, 0, original_widget)
            self.setItem(row, 1, translation_widget)

    def set_right_color(self, widget, was_correct):
        color = QColor(0, 128, 0) if was_correct else QColor(255, 0, 0)
        widget.setForeground(color)