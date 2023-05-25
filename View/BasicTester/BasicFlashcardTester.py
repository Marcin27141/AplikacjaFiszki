from PySide6.QtWidgets import QWidget, QStackedLayout, QWidget
from View.BasicTester.BasicIncorrectWidget import BasicIncorrectWidget
from View.BasicTester.BasicResultWidget import BasicResultWidget
from View.BasicTester.BasicTestWidget import BasicTestWidget

class BasicFlashcardTester(QWidget):
    RESULT_DISPLAY_TIME = 1

    def __init__(self, controller, flashcards) -> None:
        super().__init__()
        self.controller = controller
        
        self.test_widget = BasicTestWidget(self.controller, flashcards)
        self.mistake_widget = BasicIncorrectWidget(self.controller)
        self.result_widget = BasicResultWidget(self.controller)

        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(self.test_widget)
        self.stacked_layout.addWidget(self.mistake_widget)
        self.stacked_layout.addWidget(self.result_widget)
        self.setLayout(self.stacked_layout)