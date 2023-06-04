from PySide6.QtWidgets import QWidget, QStackedLayout, QWidget
from PySide6.QtCore import Qt, Signal
from View.BasicTester.BasicIncorrectWidget import BasicIncorrectWidget
from View.BasicTester.BasicResultWidget import BasicResultWidget
from View.BasicTester.BasicTestWidget import BasicTestWidget

class BasicFlashcardTesterSwitch(QWidget):
    #RESULT_DISPLAY_TIME = 1
    RETURN_TO_MENU = Signal()

    def __init__(self, test_widget, mistake_widget, result_widget) -> None:
        super().__init__()
        
        self.test_widget = test_widget
        self.test_widget.DISPLAY_INCORRECT_ANSWER.connect(lambda incorrect_answer: self.show_incorrect_answer(incorrect_answer))
        self.test_widget.SHOW_TEST_SUMMARY_VIEW.connect(self.show_test_summary)
        self.test_widget.RETURN_TO_MENU.connect(self.RETURN_TO_MENU.emit)

        self.mistake_widget = mistake_widget
        self.mistake_widget.GO_BACK_TO_TESTING.connect(self.go_back_to_testing)

        self.result_widget = result_widget
        self.result_widget.RETURN_TO_MENU.connect(self.RETURN_TO_MENU.emit)
        self.result_widget.RETAKE_THE_TEST.connect(self.retake_the_test)

        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(self.test_widget)
        self.stacked_layout.addWidget(self.mistake_widget)
        self.stacked_layout.addWidget(self.result_widget)
        self.setLayout(self.stacked_layout)

    def reset(self, strong = False):
        self.test_widget.reset(strong)
        self.stacked_layout.setCurrentWidget(self.test_widget)
        self.test_widget.setEnabled(True)

    def show_incorrect_answer(self, incorrect_answer):
        self.mistake_widget.present_incorrect_answer(incorrect_answer)
        self.stacked_layout.setCurrentWidget(self.mistake_widget)
        self.test_widget.setEnabled(False)
        self.mistake_widget.setEnabled(True)

    def go_back_to_testing(self):
        self.stacked_layout.setCurrentWidget(self.test_widget)
        self.test_widget.setEnabled(True)
        self.mistake_widget.setEnabled(False)
        self.test_widget.show_next_flashcard()

    def show_test_summary(self):
        self.stacked_layout.setCurrentWidget(self.result_widget)
        self.test_widget.setEnabled(False)

    def retake_the_test(self):
        self.test_widget.reset(True)
        self.stacked_layout.setCurrentWidget(self.test_widget)
        self.test_widget.setEnabled(True)