from PySide6.QtWidgets import QWidget, QVBoxLayout, QGridLayout , QWidget, QLabel, QPushButton, QSizePolicy
from PySide6.QtCore import Qt, QTimer, Signal
from View.TimeTester.TimerWidget import TimerWidget
from View.ViewUtilities import set_widget_font_size
import random

class TimeTestWidget(QWidget):
    RESULT_DISPLAY_TIME = 2
    NUM_OF_POSSIBILITIES = 4
    TIME_FOR_ANSWER = 5
    RETURN_TO_MENU = Signal()
    SHOW_TEST_SUMMARY_VIEW = Signal()

    def __init__(self) -> None:
        super().__init__()
        self.flashcard_index = 0
        self.flashcards = []

        self.timer_widget = TimerWidget(self.TIME_FOR_ANSWER)
        self.timer_widget.TIMEOUT_SIGNAL.connect(self.answer_not_given)

        self.original_label = QLabel()
        
        self.response_buttons = [QPushButton() for _ in range(self.NUM_OF_POSSIBILITIES)]
        size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        for button in self.response_buttons:
            button.clicked.connect(self.check_answer)
            button.setSizePolicy(size_policy)

        grid_layout = QGridLayout()
        for row in range(int(len(self.response_buttons)/2)):
            grid_layout.addWidget(self.response_buttons[(row*2)], row, 0)
            grid_layout.addWidget(self.response_buttons[(row*2)+1], row, 1)
        self.response_widget = QWidget()
        self.response_widget.setLayout(grid_layout)

        self.return_button = QPushButton("Return")
        self.return_button.clicked.connect(self.go_back_to_menu)
        set_widget_font_size(self.return_button, 20)

        test_layout = QVBoxLayout()
        test_layout.addWidget(self.timer_widget)
        test_layout.addWidget(self.original_label)
        test_layout.addWidget(self.response_widget)
        test_layout.addWidget(self.return_button)
        self.setLayout(test_layout)

    def go_back_to_menu(self):
        self.timer_widget.stop()
        self.RETURN_TO_MENU.emit()

    def load_flashcards_for_learning(self, flashcards_set):
        self.flashcards_set = flashcards_set
        self.flashcards = flashcards_set.flashcards
        self.initialize_flashcard_label()
        self.load_answer_buttons()
        self.timer_widget.start()

    def load_answer_buttons(self):
        right_answer = self.get_current_flashcard().translation
        other_flashcards = self.flashcards[:self.flashcard_index] + self.flashcards[self.flashcard_index + 1:]
        incorrect_answers = random.sample(other_flashcards, self.NUM_OF_POSSIBILITIES - 1)
        self.correct_button = random.sample(self.response_buttons, 1)[0]
        self.correct_button.setText(right_answer)
        incorrect_buttons = [_button for _button in self.response_buttons if _button != self.correct_button]
        for idx, _button in enumerate(incorrect_buttons):
            _button.setText(incorrect_answers[idx].translation)

    def initialize_flashcard_label(self):
        set_widget_font_size(self.original_label, 20)
        self.original_label.setAlignment(Qt.AlignHCenter)
        if self.flashcards: self.original_label.setText(self.flashcards[0].original)

    def get_current_flashcard(self):
        return self.flashcards[self.flashcard_index]

    def check_answer(self):
        self.timer_widget.stop()
        button = self.sender()
        is_correct = self.get_current_flashcard().test_answer(button.text())
        self.display_result(is_correct, button)
    
    def show_correct_answer(self):
        self.correct_button.setStyleSheet(f"background-color: green;color: white")
        self.correct_button.repaint()

    def display_result(self, is_correct, button):
        background_color = 'green' if is_correct else 'red'
        text_color = 'black' if is_correct else 'white'
        button.setStyleSheet(f"background-color: {background_color};color: {text_color}")
        button.repaint()
        if not is_correct: self.show_correct_answer()
        QTimer.singleShot(self.RESULT_DISPLAY_TIME * 1000, self.show_next_flashcard)

    def answer_not_given(self):
        self.show_correct_answer()
        self.get_current_flashcard().tested_incorrect()
        incorrect_buttons = [_button for _button in self.response_buttons if _button != self.correct_button]
        for incorrect_button in incorrect_buttons:
            incorrect_button.setStyleSheet(f"background-color: red; color: white")
            incorrect_button.repaint()
        QTimer.singleShot(self.RESULT_DISPLAY_TIME * 1000, self.show_next_flashcard)

    def reset_buttons_colors(self):
        for button in self.response_buttons:
            button.setStyleSheet(f"background-color: white;color: black")

    def show_next_flashcard(self):
        if self.flashcard_index < len(self.flashcards) - 1:
            self.flashcard_index += 1
            self.original_label.setText(self.get_current_flashcard().original)
            self.reset_buttons_colors()
            self.load_answer_buttons()
            self.timer_widget.reset()
            self.timer_widget.start()
        else:
            self.show_test_summary()

    def show_test_summary(self):
        self.timer_widget.stop()
        self.SHOW_TEST_SUMMARY_VIEW.emit()

    def reset(self, strong = False):
        self.flashcard_index = 0
        self.initialize_flashcard_label()
        self.reset_buttons_colors()
        self.timer_widget.reset()
        self.timer_widget.start()