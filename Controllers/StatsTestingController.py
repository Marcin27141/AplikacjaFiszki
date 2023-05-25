from Controllers.BasicTestingController import TestingController
from View.StatsTester.StatsResultWidget import TestResults

class StatsTestingController(TestingController):
    def __init__(self) -> None:
        super().__init__()
    
    def set_test_widget(self, tester_widget):
        super().set_test_widget(tester_widget)

    def show_test_summary(self, all, correct, incorrect):
        self.tester_widget.result_widget.present_results(TestResults(all, correct, incorrect))
        self.tester_widget.stacked_layout.setCurrentWidget(self.tester_widget.result_widget)
        self.tester_widget.test_widget.setEnabled(False)