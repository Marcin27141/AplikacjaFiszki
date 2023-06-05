from PySide6.QtCore import Qt, Signal
from View.TimeTester.TimeTestWidget import TimeTestWidget
from View.StatsTester.StatsTestWidget import TestResults

class TimeTestStatsWidget(TimeTestWidget):
    SHOW_TEST_SUMMARY_VIEW = Signal(object)

    def __init__(self, controller) -> None:
        super().__init__()
        self.controller = controller
        self.original_flashcards = []
        self.flashcards_correct = []
        self.flashcards_incorrect = []

    def load_flashcards_for_learning(self, flashcards_set):
        self.original_flashcards = flashcards_set.flashcards
        super().load_flashcards_for_learning(flashcards_set)

    def check_answer(self):
        button = self.sender()
        is_correct = self.get_current_flashcard().test_answer(button.text())
        if is_correct:
            self.flashcards_correct.append(self.get_current_flashcard())
        else:
            self.flashcards_incorrect.append(self.get_current_flashcard())
        super().check_answer()

    def answer_not_given(self):
        self.flashcards_incorrect.append(self.get_current_flashcard())
        return super().answer_not_given()

    def show_test_summary(self):
        self.controller.update_set_statistics(self.flashcards_set)
        self.SHOW_TEST_SUMMARY_VIEW.emit(TestResults(
            self.flashcards,
            self.flashcards_correct,
            self.flashcards_incorrect
            ))

    def set_flashcards(self, new_flashcards):
        self.flashcards = new_flashcards

    def go_back_to_menu(self):
        self.controller.update_set_statistics(self.flashcards_set)
        return super().go_back_to_menu()

    def reset(self, strong = False):
        if strong: self.flashcards = self.original_flashcards
        self.flashcards_correct = []
        self.flashcards_incorrect = []
        super().reset()