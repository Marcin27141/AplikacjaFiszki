from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout, QPushButton, QLabel, QTextEdit
from View.BasicTester.BasicFlashcardTester import BasicFlashcardTester
from View.StatsTester.StatsFlashcardTester import StatsFlashcardTester
from Controllers.BasicTestingController import TestingController
from Controllers.StatsTestingController import StatsTestingController
from Controllers.FlashcardsSetController import FlashcardsSetController
from View.FlashcardsSets.FlashcardsSetSwitchWidget import FlashcardsSetSwitchWidget

class ApplicationLayout(QVBoxLayout):
    def __init__(self, db_manager):
        super().__init__()

        """#test_controller = TestingController()
        #self.tester = BasicFlashcardTester(test_controller, flashcards)
        test_controller = StatsTestingController()
        self.tester = StatsFlashcardTester(test_controller, flashcards)

        test_controller.set_test_widget(self.tester)
        self.addWidget(self.tester)"""

        sets_controller = FlashcardsSetController(db_manager)
        self.flashcards_set_widget = FlashcardsSetSwitchWidget(sets_controller)
        sets_controller.set_flashcards_widget(self.flashcards_set_widget)

        self.addWidget(self.flashcards_set_widget)
