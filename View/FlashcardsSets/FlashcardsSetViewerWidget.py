from PySide6.QtWidgets import QWidget, QTableWidget, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QMessageBox
from PySide6.QtCore import Qt, Signal, QObject
from View.FlashcardsSets.FlashcardsSetListTable import FlashcardsSetListTable
from View.FlashcardsSets.NameWidget import NameWidget
from Model.Flashcards import Flashcard
from View.ViewUtilities import set_widget_font_size

class FlashcardsSetViewerWidget(QWidget):
    SHOW_CREATE_SET_VIEW = Signal()
    SHOW_SET_DETAILS_VIEW = Signal(object)

    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.view_table_widget = FlashcardsSetListTable(controller)
        self.view_table_widget.SHOW_SET_DETAILS_VIEW.connect(lambda flashcards: self.SHOW_SET_DETAILS_VIEW.emit(flashcards))
        
        self.new_set_button = QPushButton("New Set")
        self.new_set_button.clicked.connect(lambda: self.SHOW_CREATE_SET_VIEW.emit())

        layout = QVBoxLayout()
        layout.addWidget(self.view_table_widget)
        layout.addWidget(self.new_set_button)
        self.setLayout(layout)