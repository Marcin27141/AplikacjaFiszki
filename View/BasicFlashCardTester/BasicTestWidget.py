from PySide6.QtWidgets import QWidget, QVBoxLayout, QStackedLayout, QWidget, QLabel, QLineEdit, QPushButton
from PySide6.QtCore import Qt, QTimer
from View.ViewUtilities import set_widget_font_size
from View.BasicFlashCardTester.BasicIncorrectWidget import BasicIncorrectWidget
from View.BasicFlashCardTester.BasicResultWidget import BasicResultWidget

class BasicTestWidget(QWidget):
    RESULT_DISPLAY_TIME = 1

    def __init__(self, controller, flashcards) -> None:
        super().__init__()
        self.controller = controller
        self.flashcards = flashcards
        self.flashcard_index = 0

        self.original_label = QLabel()
        self.initialize_flashcard_label()
        
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

    def initialize_flashcard_label(self):
        set_widget_font_size(self.original_label, 20)
        self.original_label.setAlignment(Qt.AlignHCenter)
        if len(self.flashcards) > 0: self.original_label.setText(self.flashcards[0].original)

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
            self.display_answer_incorrect()
        
    def display_answer_correct(self):
        self.result_label.setText("CORRECT!")
        self.result_label.setStyleSheet("color: green;")
        QTimer.singleShot(self.RESULT_DISPLAY_TIME * 1000, self.show_next_flashcard)

    def display_answer_incorrect(self):
        self.controller.change_to_mistake_layout(self.translation_text.text(), self.get_current_flashcard())

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
        self.controller.show_test_summary()

    def reset(self):
        self.flashcard_index = 0
        self.initialize_flashcard_label()
        self.result_label.clear()
        self.translation_text.clear()
        self.translation_text.setFocus()