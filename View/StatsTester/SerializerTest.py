from View.BasicTester.BasicTestWidget import BasicTestWidget
from PySide6.QtCore import Qt, Signal
from View.StatsTester.StatsTestWidget import StatsTestWidget

class SerializerTest(StatsTestWidget):
    def __init__(self, serialize_controller) -> None:
        super().__init__()
        self.serialize_controller = serialize_controller

    def return_to_menu(self):
        if self.original_flashcards != self.flashcards or self.flashcard_index > 0:
            self.serialize_controller.serialize_test(self.flashcards_set.name, self)
        self.RETURN_TO_MENU.emit()

    def load_test(self, test_to_load):
        self.flashcard_index = test_to_load.flashcard_index
        self.flashcards_set = test_to_load.flashcards_set
        self.flashcards = test_to_load.flashcards
        self.original_flashcards = test_to_load.original_flashcards
        self.flashcards_correct = test_to_load.flashcards_correct
        self.flashcards_incorrect = test_to_load.flashcards_incorrect
        self.initialize_flashcard_label()