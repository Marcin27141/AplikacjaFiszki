from PySide6.QtWidgets import QVBoxLayout
import Controllers.FlashcardsSetController as flashcards_controllers
from View.FlashcardsSets.FlashcardsSetSwitchWidget import FlashcardsSetSwitchWidget
from View.FlashcardsSets.FlashcardsSetStatsViewerWidget import FlashcardsSetStatsViewerWidget

class ApplicationLayout(QVBoxLayout):
    def __init__(self, db_manager):
        super().__init__()

        sets_controller = flashcards_controllers.FlashcardsSetController()
        self.flashcards_set_widget = FlashcardsSetSwitchWidget(sets_controller)
        self.addWidget(self.flashcards_set_widget)
