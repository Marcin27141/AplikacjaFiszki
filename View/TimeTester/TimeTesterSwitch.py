from PySide6.QtWidgets import QWidget, QStackedLayout, QWidget
from PySide6.QtCore import Qt, Signal
from View.TimeTester.TimeTestWidget import TimeTestWidget
from View.StatsTester.StatsResultWidget import StatsResultWidget
from View.BasicTester.BasicResultWidget import BasicResultWidget

class TimeTesterSwitch(QWidget):
    RETURN_TO_MENU = Signal()

    def __init__(self) -> None:
        super().__init__()
        
        self.test_widget = TimeTestWidget()
        self.test_widget.SHOW_TEST_SUMMARY_VIEW.connect(self.show_test_summary)

        self.result_widget = BasicResultWidget()
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

    def show_test_summary(self):
        self.stacked_layout.setCurrentWidget(self.result_widget)
        self.test_widget.setEnabled(False)

    def retake_the_test(self):
        self.test_widget.reset(True)
        self.stacked_layout.setCurrentWidget(self.test_widget)
        self.test_widget.setEnabled(True)