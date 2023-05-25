from View.BasicTester.BasicFlashcardTester import BasicFlashcardTester
from View.BasicTester.BasicIncorrectWidget import IncorrectAnswer

class TestingController:
    def set_test_widget(self, tester_widget):
        self.tester_widget = tester_widget

    def change_to_mistake_layout(self, given_answer, flashcard):
        self.tester_widget.mistake_widget.present_incorrect_answer(IncorrectAnswer(
            flashcard,
            given_answer
        ))
        self.tester_widget.stacked_layout.setCurrentWidget(self.tester_widget.mistake_widget)
        self.tester_widget.test_widget.setEnabled(False)

    def go_back_to_testing(self):
        self.tester_widget.stacked_layout.setCurrentWidget(self.tester_widget.test_widget)
        self.tester_widget.test_widget.setEnabled(True)
        self.tester_widget.test_widget.show_next_flashcard()

    def show_test_summary(self):
        self.tester_widget.stacked_layout.setCurrentWidget(self.tester_widget.result_widget)
        self.tester_widget.test_widget.setEnabled(False)

    def retake_the_test(self):
        self.tester_widget.test_widget.reset()
        self.tester_widget.stacked_layout.setCurrentWidget(self.tester_widget.test_widget)
        self.tester_widget.test_widget.setEnabled(True)