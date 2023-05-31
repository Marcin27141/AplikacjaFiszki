from PySide6.QtWidgets import QWidget, QVBoxLayout, QGridLayout , QWidget, QLabel, QLineEdit, QPushButton, QSizePolicy
from PySide6.QtCore import Qt, QTimer, Signal
from View.ViewUtilities import set_widget_font_size
import random

class TimeTestWidget(QWidget):
    RESULT_DISPLAY_TIME = 1
    NUM_OF_POSSIBILITIES = 4
    TIME_FOR_ANSWER = 5
    SHOW_TEST_SUMMARY_VIEW = Signal()

    def __init__(self) -> None:
        super().__init__()
        self.flashcard_index = 0
        self.flashcards = []
        self.original_label = QLabel()
        
        self.response_buttons = [QPushButton() for _ in range(self.NUM_OF_POSSIBILITIES)]
        size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        for button in self.response_buttons:
            button.clicked.connect(self.check_answer)
            button.setSizePolicy(size_policy)
        #self.initialize_responses()

        grid_layout = QGridLayout()
        for row in range(int(len(self.response_buttons)/2)):
            grid_layout.addWidget(self.response_buttons[(row*2)], row, 0)
            grid_layout.addWidget(self.response_buttons[(row*2)+1], row, 1)
        self.response_widget = QWidget()
        self.response_widget.setLayout(grid_layout)

        test_layout = QVBoxLayout()
        test_layout.addWidget(self.original_label)
        test_layout.addWidget(self.response_widget)
        self.setLayout(test_layout)

    def load_flashcards_for_learning(self, flashcards_set):
        self.flashcards = flashcards_set.flashcards
        self.initialize_flashcard_label()
        self.initialize_answer_buttons()

    def initialize_answer_buttons(self):
        right_answer = self.get_current_flashcard().translation
        other_flashcards = self.flashcards[:self.flashcard_index] + self.flashcards[self.flashcard_index + 1:]
        incorrect_answers = random.sample(other_flashcards, self.NUM_OF_POSSIBILITIES - 1)
        correct_button = random.sample(self.response_buttons, 1)[0]
        correct_button.setText(right_answer)
        incorrect_buttons = [_button for _button in self.response_buttons if _button != correct_button]
        for idx, _button in enumerate(incorrect_buttons):
            _button.setText(incorrect_answers[idx].translation)

    def initialize_flashcard_label(self):
        set_widget_font_size(self.original_label, 20)
        self.original_label.setAlignment(Qt.AlignHCenter)
        if self.flashcards: self.original_label.setText(self.flashcards[0].original)

    def get_current_flashcard(self):
        return self.flashcards[self.flashcard_index]

    def check_answer(self, button):
        button = self.sender()
        is_correct = self.get_current_flashcard().test_answer(button.text())
        self.display_result(is_correct, button)
        
    def display_result(self, is_correct, button):
        #TODO fix, not working
        back_color = 'green' if is_correct else 'red'
        text_color = 'black' if is_correct else 'white'
        button.setStyleSheet(f"background-color: {back_color};color: {text_color}")
        button.repaint()
        QTimer.singleShot(self.RESULT_DISPLAY_TIME * 1000, self.show_next_flashcard)

    def reset_buttons_colors(self):
        for button in self.response_buttons:
            button.setStyleSheet(f"background-color: white;color: black")

    def show_next_flashcard(self):
        self.reset_buttons_colors()
        if self.flashcard_index < len(self.flashcards) - 1:
            self.flashcard_index += 1
            self.original_label.setText(self.get_current_flashcard().original)
        else:
            self.show_test_summary()

    def show_test_summary(self):
        self.SHOW_TEST_SUMMARY_VIEW.emit()

    def reset(self, strong = False):
        self.flashcard_index = 0
        self.initialize_flashcard_label()