from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout, QPushButton, QLabel, QWidget
from View.ViewUtilities import set_widget_font_size
from View.StatsTester.TestedWordsListWidget import TestedWordsListWidget

class TestResults:
    def __init__(self, all_flashcards, correct_flascards, incorrect_flashcards) -> None:
        self.all_flashcards = all_flashcards
        self.correct_flashcards = correct_flascards
        self.incorrect_flashcards = incorrect_flashcards

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

        self.tested_words_widget = TestedWordsListWidget()

        self.continue_button = QPushButton()

        widget_layout = QVBoxLayout()
        widget_layout.addWidget(self.title_label)
        widget_layout.addWidget(self.all_flashcards_label)
        widget_layout.addWidget(self.correct_flashcards_label)
        widget_layout.addWidget(self.incorrect_flashcards_label)
        widget_layout.addWidget(self.tested_words_widget)
        widget_layout.addWidget(self.continue_button)
        self.setLayout(widget_layout)

    def initialize_title_label(self):
        set_widget_font_size(self.title_label, 20)
        self.title_label.setAlignment(Qt.AlignHCenter)

    def present_results(self, test_results):
        self.all_flashcards_label.setText("Tested words: " + str(len(test_results.all_flashcards)))
        self.correct_flashcards_label.setText("Words correct: " + str(len(test_results.correct_flashcards)))
        self.incorrect_flashcards_label.setText("Words incorrect: " + str(len(test_results.incorrect_flashcards)))
        self.tested_words_widget.present_tested_flashcards([(flashcard, flashcard in test_results.correct_flashcards) for flashcard in test_results.all_flashcards])
        self.present_the_button(len(test_results.incorrect_flashcards) == 0)

    def present_the_button(self, is_over):
        if is_over:
            self.continue_button.setText("Try Again")
            self.continue_button.clicked.connect(self.retake_the_test)
        else:
            self.continue_button.setText("Continue")
            self.continue_button.clicked.connect(self.continue_the_test)

    def continue_the_test(self):
        self.controller.continue_the_test()

    def retake_the_test(self):
        self.controller.retake_the_test()