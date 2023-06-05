from PySide6.QtWidgets import QWidget, QWidget, QPushButton, QVBoxLayout
from View.FlashcardsSets.FlashcardsSetStatsTable import FlashcardSetStatsTable
from PySide6.QtCore import Qt, Signal
from View.FlashcardsSets.FlashcardsSetStatsTable import FlashcardSetStatsTable

class FlashcardsSetStatsViewerWidget(QWidget):
    RETURN_TO_MENU = Signal()
    
    def __init__(self):
        super().__init__()
        
        self.table_widget = FlashcardSetStatsTable()

        self.return_button = QPushButton("Return")
        self.return_button.clicked.connect(lambda: self.RETURN_TO_MENU.emit())

        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)
        layout.addWidget(self.return_button)
        self.setLayout(layout)

    def load_set_for_stats(self, flashcards_set):
        self.table_widget.load_set_for_viewing(flashcards_set)

    """def showEvent(self, event):
        self.setFocus()
        super().showEvent(event)
        self.table_widget.clearContents()
        self.table_widget.setRowCount(1)"""