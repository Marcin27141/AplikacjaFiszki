from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout, QPushButton, QLabel, QTextEdit
from View.BasicTester.BasicFlashcardTester import BasicFlashcardTester
from View.StatsTester.StatsFlashcardTester import StatsFlashcardTester
from Controllers.BasicTestingController import TestingController
from Controllers.StatsTestingController import StatsTestingController

class ApplicationLayout(QVBoxLayout):
    def __init__(self, flashcards):
        super().__init__()

        #test_controller = TestingController()
        #self.tester = BasicFlashcardTester(test_controller, flashcards)
        test_controller = StatsTestingController()
        self.tester = StatsFlashcardTester(test_controller, flashcards)

        test_controller.set_test_widget(self.tester)
        self.addWidget(self.tester)