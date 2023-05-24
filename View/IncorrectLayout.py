from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout, QPushButton, QLabel
from View.ViewUtilities import set_widget_font_size

class IncorrectLayout(QVBoxLayout):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.incorrect_label = QLabel("INCORRECT!")
        self.initialize_incorrect_label()

        self.original_label = QLabel()
        self.initialize_original_label()

        self.given_answer_label = QLabel()
        self.initialize_given_answer_label()

        self.translation_label = QLabel()
        self.initialize_translation_label()

        self.button = QPushButton("Got it!")
        self.button.clicked.connect(self.go_back_to_testing)

        self.addWidget(self.incorrect_label)
        self.addWidget(self.original_label)
        self.addWidget(self.given_answer_label)
        self.addWidget(self.translation_label)
        self.addWidget(self.button)

    def initialize_incorrect_label(self):
        set_widget_font_size(self.incorrect_label, 20)
        self.incorrect_label.setAlignment(Qt.AlignHCenter)
        self.incorrect_label.setStyleSheet("color: red;")

    def initialize_given_answer_label(self):
        set_widget_font_size(self.incorrect_label, 15)

    def initialize_original_label(self):
        set_widget_font_size(self.incorrect_label, 15)
        #self.result_label.setAlignment(Qt.AlignHCenter)

    def initialize_translation_label(self):
        set_widget_font_size(self.incorrect_label, 15)
        #self.result_label.setAlignment(Qt.AlignHCenter)

    def fill_mistake_info(self, flashcard, given_answer):
        self.original_label.setText("Tested word: " + flashcard.original)
        self.given_answer_label.setText("Your answer: " + given_answer)
        self.translation_label.setText("Correct translation: " + flashcard.translation)

    def go_back_to_testing(self):
        self.controller.go_back_to_testing()
