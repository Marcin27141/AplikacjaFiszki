from View.BasicFlashcardTester import BasicFlashcardTester

class TestingController:
    def set_test_widget(self, test_widget):
        self.test_widget = test_widget

    def change_to_mistake_layout(self, given_answer, flashcard):
        self.test_widget.mistake_widget.layout().fill_mistake_info(flashcard, given_answer)
        self.test_widget.stacked_layout.setCurrentWidget(self.test_widget.mistake_widget)

    def go_back_to_testing(self):
        self.test_widget.stacked_layout.setCurrentWidget(self.test_widget.test_widget)

    def show_test_summary(self):
        self.test_widget.stacked_layout.setCurrentWidget(self.test_widget.result_widget)

    def retake_the_test(self):
        self.test_widget.reset()
        self.test_widget.stacked_layout.setCurrentWidget(self.test_widget.test_widget)