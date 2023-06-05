from View.BasicTester.BasicTestWidget import BasicTestWidget
from PySide6.QtCore import Qt, Signal
class TestResults:
    def __init__(self, all_flashcards, correct_flascards, incorrect_flashcards) -> None:
        self.all_flashcards = all_flashcards
        self.correct_flashcards = correct_flascards
        self.incorrect_flashcards = incorrect_flashcards

class StatsTestWidget(BasicTestWidget):
    SHOW_TEST_SUMMARY_VIEW = Signal(object)

    def __init__(self, controller) -> None:
        super().__init__()
        self.controller = controller
        self.original_flashcards = []
        self.flashcards_correct = []
        self.flashcards_incorrect = []

    def __getstate__(self):
        state = super().__getstate__()
        state_dict = {
            'basic_test': state,
            'stats_test': (self.original_flashcards, self.flashcards_correct, self.flashcards_incorrect)
        }
        return state_dict

    def __setstate__(self, state):
        super().__setstate__(state['basic_test'])
        self.original_flashcards, self.flashcards_correct, self.flashcards_incorrect = state['stats_test']

    def load_flashcards_for_learning(self, flashcards_set):
        super().load_flashcards_for_learning(flashcards_set)
        self.original_flashcards = flashcards_set.flashcards

    def check_answer(self):
        super().check_answer()
        is_correct = self.flashcards[self.flashcard_index].test_answer(self.translation_text.text())
        if is_correct:
            self.flashcards_correct.append(self.get_current_flashcard())
        else:
            self.flashcards_incorrect.append(self.get_current_flashcard())

    def show_test_summary(self):
        self.controller.update_set_statistics(self.flashcards_set)
        self.SHOW_TEST_SUMMARY_VIEW.emit(TestResults(
            self.flashcards,
            self.flashcards_correct,
            self.flashcards_incorrect
            ))

    def set_flashcards(self, new_flashcards):
        self.flashcards = new_flashcards

    def return_to_menu(self):
        self.controller.update_set_statistics(self.flashcards_set)
        self.RETURN_TO_MENU.emit()

    def reset(self, strong = False):
        if strong: self.flashcards = self.original_flashcards
        self.flashcards_correct = []
        self.flashcards_incorrect = []
        super().reset()