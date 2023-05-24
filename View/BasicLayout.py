from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout, QPushButton, QLabel, QTextEdit
from View.BasicFlashcardTester import BasicFlashcardTester

class ApplicationLayout(QVBoxLayout):
    def __init__(self, flashcards):
        super().__init__()
        self.tester = BasicFlashcardTester(flashcards)
        self.addWidget(self.tester)