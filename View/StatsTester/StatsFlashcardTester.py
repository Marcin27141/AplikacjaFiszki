from PySide6.QtWidgets import QWidget, QStackedLayout, QWidget
from View.StatsTester.StatsResultWidget import StatsResultWidget
from View.StatsTester.StatsIncorrectWidget import StatsIncorrectWidget
from View.StatsTester.StatsTestWidget import StatsTestWidget

class StatsFlashcardTester(QWidget):
    RESULT_DISPLAY_TIME = 1

    def __init__(self, controller, flashcards) -> None:
        super().__init__()
        self.controller = controller

        self.test_widget = StatsTestWidget(self.controller, flashcards)
        self.mistake_widget = StatsIncorrectWidget(self.controller)
        self.result_widget = StatsResultWidget(self.controller)

        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(self.test_widget)
        self.stacked_layout.addWidget(self.mistake_widget)
        self.stacked_layout.addWidget(self.result_widget)
        self.setLayout(self.stacked_layout)