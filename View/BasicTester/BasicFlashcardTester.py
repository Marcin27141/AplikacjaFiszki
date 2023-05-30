from PySide6.QtWidgets import QWidget, QStackedLayout, QWidget
from PySide6.QtCore import Qt, Signal
from View.BasicTester.BasicFlashcardTesterSwitch import BasicFlashcardTesterSwitch
from View.BasicTester.BasicIncorrectWidget import BasicIncorrectWidget
from View.BasicTester.BasicResultWidget import BasicResultWidget
from View.BasicTester.BasicTestWidget import BasicTestWidget

class BasicFlashcardTester(BasicFlashcardTesterSwitch):
    def __init__(self) -> None:
        test_widget = BasicTestWidget()
        result_widget = BasicResultWidget()
        mistake_widget = BasicIncorrectWidget()
        super().__init__(test_widget, mistake_widget, result_widget)