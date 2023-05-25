from View.BasicTester.BasicTestWidget import BasicTestWidget

class StatsTestWidget(BasicTestWidget):
    def __init__(self, controller, flashcards) -> None:
        super().__init__(controller, flashcards)
        self.flashcards_correct = []
        self.flashcards_incorrect = []

    def check_answer(self):
        super().check_answer()
        is_correct = self.flashcards[self.flashcard_index].test_answer(self.translation_text.text())
        if is_correct:
            self.flashcards_correct.append(self.get_current_flashcard())
        else:
            self.flashcards_incorrect.append(self.get_current_flashcard())

    def show_test_summary(self):
        self.controller.show_test_summary(
            self.flashcards,
            self.flashcards_correct,
            self.flashcards_incorrect
            )

    def set_flashcards(self, new_flashcards):
        self.flashcards = new_flashcards

    def reset(self):
        super().reset()
        self.flashcards_correct = []
        self.flashcards_incorrect = []