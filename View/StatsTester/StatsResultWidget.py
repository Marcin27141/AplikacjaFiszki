from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout, QPushButton, QLabel, QWidget
from View.ViewUtilities import set_widget_font_size

class TestResults:
    def __init__(self, num_of_all, num_of_correct, num_of_incorrect) -> None:
        self.num_of_all = num_of_all
        self.num_of_correct = num_of_correct
        self.num_of_incorrect = num_of_incorrect

class StatsResultWidget(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title_label = QLabel("Your results:")
        self.initialize_title_label()

        self.all_flashcards_label = QLabel()
        set_widget_font_size(self.all_flashcards_label, 15)

        self.correct_flashcards_label = QLabel()
        set_widget_font_size(self.correct_flashcards_label, 15)

        self.incorrect_flashcards_label = QLabel()
        set_widget_font_size(self.incorrect_flashcards_label, 15)

        self.again_button = QPushButton("Try again")
        self.again_button.clicked.connect(self.retake_the_test)

        widget_layout = QVBoxLayout()
        widget_layout.addWidget(self.title_label)
        widget_layout.addWidget(self.all_flashcards_label)
        widget_layout.addWidget(self.correct_flashcards_label)
        widget_layout.addWidget(self.incorrect_flashcards_label)
        widget_layout.addWidget(self.again_button)
        self.setLayout(widget_layout)

    def initialize_title_label(self):
        set_widget_font_size(self.title_label, 20)
        self.title_label.setAlignment(Qt.AlignHCenter)

    def present_results(self, test_results):
        self.all_flashcards_label.setText("Tested words: " + str(test_results.num_of_all))
        self.correct_flashcards_label.setText("Words correct: " + str(test_results.num_of_correct))
        self.incorrect_flashcards_label.setText("Words incorrect: " + str(test_results.num_of_incorrect))

    def retake_the_test(self):
        self.controller.retake_the_test()