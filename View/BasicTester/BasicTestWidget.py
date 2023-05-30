from PySide6.QtWidgets import QWidget, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton
from PySide6.QtCore import Qt, QTimer, Signal
from View.ViewUtilities import set_widget_font_size

class IncorrectAnswer:
    def __init__(self, flashcard, given_answer) -> None:
        self.flashcard = flashcard
        self.given_answer = given_answer

class BasicTestWidget(QWidget):
    RESULT_DISPLAY_TIME = 1
    SHOW_TEST_SUMMARY_VIEW = Signal()
    DISPLAY_INCORRECT_ANSWER = Signal(object)

    def __init__(self) -> None:
        super().__init__()
        self.flashcard_index = 0
        self.flashcards = []
        self.original_label = QLabel()
        
        self.translation_text = QLineEdit()
        self.initialize_input_text()
        self.translation_text.setFocus()
        self.translation_text.returnPressed.connect(self.check_answer)
        
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.check_answer)

        self.result_label = QLabel()
        self.initialize_result_label()

        test_layout = QVBoxLayout()
        test_layout.addWidget(self.original_label)
        test_layout.addWidget(self.translation_text)
        test_layout.addWidget(self.submit_button)
        test_layout.addWidget(self.result_label)
        self.setLayout(test_layout)

    def load_flashcards_for_learning(self, flashcards_set):
        self.flashcards = flashcards_set.flashcards
        self.initialize_flashcard_label()

    def initialize_flashcard_label(self):
        set_widget_font_size(self.original_label, 20)
        self.original_label.setAlignment(Qt.AlignHCenter)
        if self.flashcards: self.original_label.setText(self.flashcards[0].original)

    def initialize_input_text(self):
        set_widget_font_size(self.translation_text, 15)
        self.translation_text.setAlignment(Qt.AlignHCenter)
        self.translation_text.setMaximumHeight(50)

    def initialize_result_label(self):
        set_widget_font_size(self.result_label, 15)
        self.result_label.setAlignment(Qt.AlignHCenter)

    def get_current_flashcard(self):
        return self.flashcards[self.flashcard_index]

    def check_answer(self):
        is_correct = self.get_current_flashcard().test_answer(self.translation_text.text())
        if is_correct:
            self.display_answer_correct()
        else:
            self.DISPLAY_INCORRECT_ANSWER.emit(IncorrectAnswer(self.get_current_flashcard(), self.translation_text.text()))
        
    def display_answer_correct(self):
        self.result_label.setText("CORRECT!")
        self.result_label.setStyleSheet("color: green;")
        QTimer.singleShot(self.RESULT_DISPLAY_TIME * 1000, self.show_next_flashcard)

    def show_next_flashcard(self):
        if self.flashcard_index < len(self.flashcards) - 1:
            self.flashcard_index += 1
            self.original_label.setText(self.get_current_flashcard().original)
            self.translation_text.clear()
            self.translation_text.setFocus()
            self.result_label.clear()
        else:
            self.show_test_summary()

    def show_test_summary(self):
        self.SHOW_TEST_SUMMARY_VIEW.emit()

    def reset(self, strong = False):
        self.flashcard_index = 0
        self.initialize_flashcard_label()
        self.result_label.clear()
        self.translation_text.clear()
        self.translation_text.setFocus()