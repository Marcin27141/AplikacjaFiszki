from PySide6.QtWidgets import QWidget, QTableWidget, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit
from View.FlashcardsSets.FlashcardsSetListTable import FlashcardsSetListTable
from View.FlashcardsSets.NameWidget import NameWidget
from Model.Flashcards import Flashcard
from View.ViewUtilities import set_widget_font_size

class FlashcardsSetViewerWidget(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.view_table_widget = FlashcardsSetListTable(controller)
        
        self.new_set_button = QPushButton("New Set")
        self.new_set_button.clicked.connect(lambda: controller.show_create_set_view())

        layout = QVBoxLayout()
        layout.addWidget(self.view_table_widget)
        layout.addWidget(self.new_set_button)
        self.setLayout(layout)