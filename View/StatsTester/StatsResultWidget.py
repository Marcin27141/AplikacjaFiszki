from PySide6.QtCore import Qt, Signal
from View.StatsTester.BasicStatsResultWidget import BasicStatsResultWidget

class StatsResultWidget(BasicStatsResultWidget):
    CONTINUE_THE_TEST = Signal(object)

    def __init__(self):
        super().__init__()

    def present_results(self, test_results):
        super().present_results(test_results)
        self.present_again_button(len(test_results.incorrect_flashcards) == 0)

    def present_again_button(self, is_over):
        if is_over:
            self.again_button.setText("Try Again")
            self.again_button.clicked.connect(lambda: self.RETAKE_THE_TEST.emit())
        else:
            self.again_button.setText("Continue")
            self.again_button.clicked.connect(lambda: self.CONTINUE_THE_TEST.emit(self.incorrect_flashcards))