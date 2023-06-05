from PySide6.QtWidgets import QWidget, QStackedLayout, QWidget
from PySide6.QtCore import Qt, Signal
from Controllers.FlashcardsSetController import FlashcardsSetController
from View.TimeTester.TimeTestWidget import TimeTestWidget
from View.TimeTester.TimeTestStatsWidget import TimeTestStatsWidget
from View.StatsTester.StatsResultWidget import BasicStatsResultWidget
from View.BasicTester.BasicResultWidget import BasicResultWidget

class TimeTesterSwitch(QWidget):
    RETURN_TO_MENU = Signal()

    def __init__(self) -> None:
        super().__init__()
        
        #self.test_widget = TimeTestWidget()
        controller = FlashcardsSetController()
        self.test_widget = TimeTestStatsWidget(controller)
        self.test_widget.SHOW_TEST_SUMMARY_VIEW.connect(self.show_test_summary)
        self.test_widget.RETURN_TO_MENU.connect(self.RETURN_TO_MENU.emit)

        #self.result_widget = BasicResultWidget()
        self.result_widget = BasicStatsResultWidget()
        self.result_widget.RETURN_TO_MENU.connect(self.RETURN_TO_MENU.emit)
        self.result_widget.RETAKE_THE_TEST.connect(self.retake_the_test)

        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(self.test_widget)
        self.stacked_layout.addWidget(self.result_widget)
        self.setLayout(self.stacked_layout)

    def reset(self, strong = False):
        self.test_widget.reset(strong)
        self.stacked_layout.setCurrentWidget(self.test_widget)
        self.test_widget.setEnabled(True)

    def show_test_summary(self, test_results):
        self.result_widget.present_results(test_results)
        self.stacked_layout.setCurrentWidget(self.result_widget)
        self.test_widget.setEnabled(False)

    def continue_the_test(self, incorrect):
        self.test_widget.set_flashcards(incorrect)
        self.test_widget.reset()
        self.stacked_layout.setCurrentWidget(self.test_widget)
        self.test_widget.setEnabled(True)

    def retake_the_test(self):
        self.test_widget.reset(True)
        self.stacked_layout.setCurrentWidget(self.test_widget)
        self.test_widget.setEnabled(True)