from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QVBoxLayout, QPushButton, QLabel, QWidget
from View.ViewUtilities import set_widget_font_size, make_font_bold

class BasicIncorrectWidget(QWidget):
    GO_BACK_TO_TESTING = Signal()

    def __init__(self):
        super().__init__()
        self.incorrect_label = QLabel("INCORRECT!")
        self.initialize_incorrect_label()

        self.original_label = QLabel()
        self.given_answer_label = QLabel()
        self.translation_label = QLabel()

        self.button = QPushButton("Got it!")
        self.initialize_button()

        widget_layout = QVBoxLayout()
        widget_layout.addWidget(self.incorrect_label)
        widget_layout.addWidget(self.original_label)
        widget_layout.addWidget(self.given_answer_label)
        widget_layout.addWidget(self.translation_label)
        widget_layout.addSpacing(50)
        widget_layout.addWidget(self.button)
        self.setLayout(widget_layout)
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.button.click()

    def initialize_button(self):
        self.button.clicked.connect(self.GO_BACK_TO_TESTING.emit)
        set_widget_font_size(self.button, 20)

    def initialize_incorrect_label(self):
        set_widget_font_size(self.incorrect_label, 35)
        make_font_bold(self.incorrect_label)
        self.incorrect_label.setAlignment(Qt.AlignHCenter)
        self.incorrect_label.setStyleSheet("color: red;")

    def present_incorrect_answer(self, incorrect_answer):
        self.original_label.setText("Tested word: " + incorrect_answer.flashcard.original)
        set_widget_font_size(self.original_label, 18)
        self.given_answer_label.setText("Your answer: " + incorrect_answer.given_answer)
        set_widget_font_size(self.given_answer_label, 18)
        self.translation_label.setText("Correct translation: " + incorrect_answer.flashcard.translation)  
        set_widget_font_size(self.translation_label, 18)