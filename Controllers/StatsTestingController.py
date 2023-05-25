from Controllers.BasicTestingController import TestingController
from View.StatsTester.StatsResultWidget import TestResults

class StatsTestingController(TestingController):
    def __init__(self) -> None:
        super().__init__()
        self.original_flashcards = None
    
    def set_test_widget(self, tester_widget):
        super().set_test_widget(tester_widget)

    def show_test_summary(self, all, correct, incorrect):
        if self.original_flashcards == None: self.original_flashcards = all
        self.tester_widget.result_widget.present_results(TestResults(all, correct, incorrect))
        self.incorrect = incorrect if len(incorrect) > 0 else self.tester_widget.test_widget.set_flashcards(self.original_flashcards)
        self.tester_widget.stacked_layout.setCurrentWidget(self.tester_widget.result_widget)
        self.tester_widget.test_widget.setEnabled(False)

    def continue_the_test(self):
        self.tester_widget.test_widget.set_flashcards(self.incorrect)
        super().retake_the_test()