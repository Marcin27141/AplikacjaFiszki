from PySide6.QtWidgets import QWidget, QVBoxLayout, QWidget, QLabel, QTextEdit, QPushButton
from PySide6.QtCore import Qt

class BasicFlashcardTester(QWidget):
    def __init__(self, flashcards) -> None:
        super().__init__()
        self.flashcards = flashcards
        self.flashcard_index = 0
        self.original_label = QLabel()
        self.set_label_font()
        self.original_label.setAlignment(Qt.AlignHCenter)
        if len(flashcards) > 0: self.original_label.setText(self.flashcards[0].original)
        self.translation_text = QTextEdit()
        self.set_text_input_font()
        self.translation_text.setAlignment(Qt.AlignHCenter)
        self.translation_text.setMaximumHeight(50)
        self.submit_button = QPushButton("Submit")
        widget_layout = QVBoxLayout()
        widget_layout.addWidget(self.original_label)
        widget_layout.addWidget(self.translation_text)
        widget_layout.addWidget(self.submit_button)
        self.submit_button.clicked.connect(self.get_next_flashcard)
        self.setLayout(widget_layout)

    def set_label_font(self):
        font = self.original_label.font()
        font.setPointSize(20)
        self.original_label.setFont(font)

    def set_text_input_font(self):
        font = self.translation_text.font()
        font.setPointSize(15)
        self.translation_text.setFont(font)

    def get_next_flashcard(self):
        if self.flashcard_index < len(self.flashcards) - 1:
            self.flashcard_index += 1
            self.original_label.setText(self.flashcards[self.flashcard_index].original)
        self.translation_text.clear()