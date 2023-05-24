from PySide6.QtWidgets import QWidget, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton
from PySide6.QtCore import Qt, QTimer
import time

class BasicFlashcardTester(QWidget):
    RESULT_DISPLAY_TIME = 1

    def __init__(self, flashcards) -> None:
        super().__init__()
        self.flashcards = flashcards
        self.flashcard_index = 0
        self.original_label = QLabel()
        self.initialize_flashcard_label()
        
        self.translation_text = QLineEdit()
        self.initialize_input_text()
        
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.check_answer)

        self.result_label = QLabel()
        self.initialize_result_label()

        widget_layout = QVBoxLayout()
        widget_layout.addWidget(self.original_label)
        widget_layout.addWidget(self.translation_text)
        widget_layout.addWidget(self.submit_button)
        widget_layout.addWidget(self.result_label)
        self.setLayout(widget_layout)

    def initialize_flashcard_label(self):
        self.set_label_font(20)
        self.original_label.setAlignment(Qt.AlignHCenter)
        if len(self.flashcards) > 0: self.original_label.setText(self.flashcards[0].original)

    def initialize_input_text(self):
        self.set_text_input_font()
        self.translation_text.setAlignment(Qt.AlignHCenter)
        self.translation_text.setMaximumHeight(50)

    def initialize_result_label(self):
        self.set_label_font(15)
        self.result_label.setAlignment(Qt.AlignHCenter)

    def set_label_font(self, size):
        font = self.original_label.font()
        font.setPointSize(size)
        self.original_label.setFont(font)

    def set_text_input_font(self):
        font = self.translation_text.font()
        font.setPointSize(15)
        self.translation_text.setFont(font)

    def check_answer(self):
        is_correct = self.flashcards[self.flashcard_index].test_answer(self.translation_text.text())
        if is_correct:
            self.result_label.setText("CORRECT!")
            self.result_label.setStyleSheet("color: green;")
        else:
            self.result_label.setText("INCORRECT!")
            self.result_label.setStyleSheet("color: red;")
        QTimer.singleShot(self.RESULT_DISPLAY_TIME * 1000, self.clear_results)
        
    def clear_results(self):
        self.result_label.clear()
        self.show_next_flashcard()

    def show_next_flashcard(self):
        if self.flashcard_index < len(self.flashcards) - 1:
            self.flashcard_index += 1
            self.original_label.setText(self.flashcards[self.flashcard_index].original)
        self.translation_text.clear()