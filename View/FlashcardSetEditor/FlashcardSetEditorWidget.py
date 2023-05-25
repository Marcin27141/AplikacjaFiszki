from PySide6.QtWidgets import QWidget, QTableWidget, QWidget, QPushButton, QVBoxLayout
from View.FlashcardSetEditor.FlashcardSetTable import FlashcardSetTable

class FlashcardSetEditorWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.table = FlashcardSetTable()
        
        self.add_button = QPushButton("Add Flashcard")
        self.add_button.clicked.connect(lambda: self.add_flashcard())

        self.continue_button = QPushButton("Continue")
        self.continue_button.clicked.connect(lambda: self.process_flashcards())

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(self.add_button)
        layout.addWidget(self.continue_button)
        self.setLayout(layout)

    def add_flashcard(self):
        row_count = self.table.rowCount()
        self.table.insertRow(row_count)

    def process_flashcards(self):
        flashcards = []
        for row in range(self.table.rowCount()):
            original_item = self.table.item(row, 0)
            translation_item = self.table.item(row, 1)
            if original_item and translation_item:
                original_text = original_item.text()
                translation_text = translation_item.text()
                flashcards.append((original_text, translation_text))
        print(flashcards)