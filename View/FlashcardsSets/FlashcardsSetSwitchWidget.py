from PySide6.QtWidgets import QTableWidget, QLineEdit, QTableWidgetItem, QHeaderView, QStackedLayout, QWidget
from PySide6.QtCore import Qt
from View.FlashcardsSets.FlashcardsSetEditorWidget import FlashcardsSetEditorWidget
from View.FlashcardsSets.FlashcardsSetViewerWidget import FlashcardsSetViewerWidget
from View.FlashcardsSets.FlashcardsSetCreatorWidget import FlashcardsSetCreatorWidget
from View.FlashcardsSets.FlashcardsSetLearnerWidget import FlashcardsSetLearnerWidget
from View.StatsTester.StatsFlashcardTester import StatsFlashcardTester

class FlashcardsSetSwitchWidget(QWidget):
    def __init__(self, controller) -> None:
        super().__init__()
        self.controller = controller

        self.show_sets_widget = FlashcardsSetViewerWidget(self.controller)
        self.edit_sets_widget = FlashcardsSetEditorWidget(self.controller)
        self.create_sets_widget = FlashcardsSetCreatorWidget(self.controller)
        self.learn_set_widget = FlashcardsSetLearnerWidget(self.controller)
        #self.tester_widget = StatsFlashcardTester(self.controller)

        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(self.show_sets_widget)
        self.stacked_layout.addWidget(self.edit_sets_widget)
        self.stacked_layout.addWidget(self.create_sets_widget)
        self.stacked_layout.addWidget(self.learn_set_widget)
        self.setLayout(self.stacked_layout)