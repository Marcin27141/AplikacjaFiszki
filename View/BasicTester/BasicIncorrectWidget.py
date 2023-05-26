from PySide6.QtCore import Qt, QEvent
from PySide6.QtWidgets import QVBoxLayout, QPushButton, QLabel, QWidget
from View.ViewUtilities import set_widget_font_size

class IncorrectAnswer:
    def __init__(self, flashcard, given_answer) -> None:
        self.flashcard = flashcard
        self.given_answer = given_answer

class BasicIncorrectWidget(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.incorrect_label = QLabel("INCORRECT!")
        self.initialize_incorrect_label()

        self.original_label = QLabel()
        set_widget_font_size(self.incorrect_label, 15)

        self.given_answer_label = QLabel()
        set_widget_font_size(self.incorrect_label, 15)

        self.translation_label = QLabel()
        set_widget_font_size(self.incorrect_label, 15)

        self.button = QPushButton("Got it!")
        self.button.clicked.connect(self.go_back_to_testing)
        #self.installEventFilter(self)

        widget_layout = QVBoxLayout()
        widget_layout.addWidget(self.incorrect_label)
        widget_layout.addWidget(self.original_label)
        widget_layout.addWidget(self.given_answer_label)
        widget_layout.addWidget(self.translation_label)
        widget_layout.addWidget(self.button)
        self.setLayout(widget_layout)
        #self.setFocusPolicy(Qt.StrongFocus)

    """def keyPressEvent(self, event):
        if self.isEnabled() and self.isHidden() == False:
            if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
                self.button.click()"""

    """def showEvent(self, event):
        self.setFocus()
        super().showEvent(event)

    def focusInEvent(self, event):
        self.setFocus()
        super().focusInEvent(event)"""

    """def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_Return:
                self.button.click()
                return True
        return False"""

    def initialize_incorrect_label(self):
        set_widget_font_size(self.incorrect_label, 20)
        self.incorrect_label.setAlignment(Qt.AlignHCenter)
        self.incorrect_label.setStyleSheet("color: red;")

    def present_incorrect_answer(self, incorrect_answer):
        self.original_label.setText("Tested word: " + incorrect_answer.flashcard.original)
        self.given_answer_label.setText("Your answer: " + incorrect_answer.given_answer)
        self.translation_label.setText("Correct translation: " + incorrect_answer.flashcard.translation)

    def go_back_to_testing(self):
        self.controller.go_back_to_testing()       