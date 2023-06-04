from PySide6.QtWidgets import QWidget, QTableWidget, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit
from PySide6.QtCore import Qt, Signal
from PySide6.QtCore import Qt, QAbstractAnimation, QVariantAnimation, QEasingCurve
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsWidget, QGraphicsOpacityEffect
from View.FlashcardsSets.FlashcardsSetEditTable import FlashcardSetEditTable
from View.FlashcardsSets.AnimationFlashcard import AnimationFlashcard
from View.FlashcardsSets.NameWidget import NameWidget
from Model.Flashcards import Flashcard
from View.ViewUtilities import set_widget_font_size

class FlashcardsSetLearnerWidget(QWidget):
    RETURN_TO_MENU = Signal()
    
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.learn_set = None
        self.flashcard_index = 0
        self.showing_translation = False

        self.flashcard_widget = QLabel()
        set_widget_font_size(self.flashcard_widget, 64)
        self.flashcard_widget.setAlignment(Qt.AlignHCenter)

        self.left_button = QPushButton("<-")
        self.left_button.clicked.connect(lambda: self.show_previous_flashcard())

        self.flip_button = QPushButton("Flip")
        self.flip_button.clicked.connect(lambda: self.show_other_flashcard_side())

        self.rigth_button = QPushButton("->")
        self.rigth_button.clicked.connect(lambda: self.show_next_flashcard())

        navigation_buttons = QWidget()
        navigation_layout = QHBoxLayout()
        navigation_layout.addWidget(self.left_button)
        navigation_layout.addWidget(self.flip_button)
        navigation_layout.addWidget(self.rigth_button)
        navigation_buttons.setLayout(navigation_layout)

        self.return_button = QPushButton("Return")
        self.return_button.clicked.connect(lambda: self.RETURN_TO_MENU.emit())

        layout = QVBoxLayout()
        layout.addWidget(self.flashcard_widget)
        layout.addWidget(navigation_buttons)
        layout.addWidget(self.return_button)
        self.setLayout(layout)

    def load_set_for_learning(self, flashcards_set):
        self.learn_set = flashcards_set
        self.flashcard_index = 0
        self.flashcard_widget.setText(self.learn_set.flashcards[self.flashcard_index].original)

    def show_flashcard(self):
        if self.showing_translation:
            self.flashcard_widget.setText(self.learn_set.flashcards[self.flashcard_index].translation)
        else:
            self.flashcard_widget.setText(self.learn_set.flashcards[self.flashcard_index].original)

    def show_other_flashcard_side(self):
        self.showing_translation = not self.showing_translation
        self.show_flashcard()

    def show_previous_flashcard(self):
        if self.flashcard_index > 0:
            self.flashcard_index -= 1
            self.show_flashcard()
            self.make_sure_buttons_locked_if_needed()

    def show_next_flashcard(self):
        if self.flashcard_index < len(self.learn_set.flashcards)-1:
            self.flashcard_index += 1
            self.show_flashcard()
            self.make_sure_buttons_locked_if_needed()

    def make_sure_buttons_locked_if_needed(self):
        self.left_button.setEnabled(self.flashcard_index > 0)
        self.rigth_button.setEnabled(self.flashcard_index < len(self.learn_set.flashcards)-1)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space or event.key() == Qt.Key_Up or event.key() == Qt.Key_Down:
            self.flip_button.click()
        elif event.key() == Qt.Key_Left:
            self.left_button.click()
        elif event.key() == Qt.Key_Right:
            self.rigth_button.click()
        else:
            super().keyPressEvent(event)

    def showEvent(self, event):
        super().showEvent(event)
        self.setFocus()
        self.flashcard_index = 0
        self.flashcard_widget.setText(self.learn_set.flashcards[self.flashcard_index].original)
        self.make_sure_buttons_locked_if_needed()