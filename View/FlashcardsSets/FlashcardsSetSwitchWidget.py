from PySide6.QtWidgets import QTableWidget, QLineEdit, QTableWidgetItem, QHeaderView, QStackedLayout, QWidget
from PySide6.QtCore import Qt
from View.FlashcardsSets.FlashcardsSetEditorWidget import FlashcardsSetEditorWidget
from View.FlashcardsSets.FlashcardsSetViewerWidget import FlashcardsSetViewerWidget
from View.FlashcardsSets.FlashcardsSetCreatorWidget import FlashcardsSetCreatorWidget
from View.FlashcardsSets.FlashcardsSetLearnerWidget import FlashcardsSetLearnerWidget
from View.StatsTester.StatsFlashcardTester import StatsFlashcardTester
from View.TimeTester.TimeTesterSwitch import TimeTesterSwitch

class FlashcardsSetSwitchWidget(QWidget):
    def __init__(self, controller) -> None:
        super().__init__()
        self.controller = controller

        self.show_sets_widget = FlashcardsSetViewerWidget(self.controller)
        self.show_sets_widget.SHOW_CREATE_SET_VIEW.connect(lambda: self.stacked_layout.setCurrentWidget(self.create_sets_widget))
        self.show_sets_widget.SHOW_SET_DETAILS_VIEW.connect(self.show_set_details)

        self.learn_set_widget = FlashcardsSetLearnerWidget(self.controller)
        self.learn_set_widget.RETURN_TO_MENU.connect(lambda: self.stacked_layout.setCurrentWidget(self.show_sets_widget))

        self.edit_sets_widget = FlashcardsSetEditorWidget(self.controller)
        self.edit_sets_widget.RETURN_TO_MENU.connect(lambda: self.stacked_layout.setCurrentWidget(self.show_sets_widget))
        self.edit_sets_widget.SHOW_LEARN_VIEW.connect(self.show_set_for_learning)
        self.edit_sets_widget.SHOW_TEST_VIEW.connect(self.show_set_for_testing)

        self.create_sets_widget = FlashcardsSetCreatorWidget(self.controller)
        self.create_sets_widget.RETURN_TO_MENU.connect(lambda: self.stacked_layout.setCurrentWidget(self.show_sets_widget))

        #self.tester_widget = StatsFlashcardTester()
        self.tester_widget = TimeTesterSwitch()
        self.tester_widget.RETURN_TO_MENU.connect(lambda: self.stacked_layout.setCurrentWidget(self.show_sets_widget))

        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(self.show_sets_widget)
        self.stacked_layout.addWidget(self.edit_sets_widget)
        self.stacked_layout.addWidget(self.create_sets_widget)
        self.stacked_layout.addWidget(self.learn_set_widget)
        self.stacked_layout.addWidget(self.tester_widget)
        self.setLayout(self.stacked_layout)

    def show_set_for_testing(self, flashcards_set):
        self.tester_widget.reset(True)
        self.tester_widget.test_widget.load_flashcards_for_learning(flashcards_set)
        self.stacked_layout.setCurrentWidget(self.tester_widget)

    def show_set_for_learning(self, flashcards_set):
        self.learn_set_widget.load_set_for_learning(flashcards_set)
        self.stacked_layout.setCurrentWidget(self.learn_set_widget)
        
    def show_set_details(self, flashcards_set):
        self.stacked_layout.setCurrentWidget(self.edit_sets_widget)
        self.edit_sets_widget.load_set_for_edit(flashcards_set)