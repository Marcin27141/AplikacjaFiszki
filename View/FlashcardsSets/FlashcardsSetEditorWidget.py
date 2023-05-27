from PySide6.QtWidgets import QWidget, QTableWidget, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit
from View.FlashcardsSets.FlashcardsSetEditTable import FlashcardSetEditTable
from View.FlashcardsSets.NameWidget import NameWidget
from Model.Flashcards import Flashcard
from View.ViewUtilities import set_widget_font_size

class FlashcardsSetEditorWidget(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.name_widget = NameWidget()
        set_widget_font_size(self.name_widget, 15)

        self.table = FlashcardSetEditTable()
        
        self.add_button = QPushButton("Add Flashcard")
        self.add_button.clicked.connect(lambda: self.add_flashcard())

        self.remove_button = QPushButton("Remove set")
        self.remove_button.setStyleSheet("background-color: red; color: white")
        self.remove_button.clicked.connect(lambda: controller.remove_set(self.displayed_set))

        self.return_button = QPushButton("Return")
        self.return_button.clicked.connect(lambda: controller.return_from_set_editing())

        self.continue_button = QPushButton("Continue")
        self.continue_button.clicked.connect(lambda: self.process_flashcards())

        navigation_buttons = QWidget()
        navigation_layout = QHBoxLayout()
        navigation_layout.addWidget(self.return_button)
        navigation_layout.addWidget(self.continue_button)
        navigation_buttons.setLayout(navigation_layout)

        layout = QVBoxLayout()
        layout.addWidget(self.name_widget)
        layout.addWidget(self.table)
        layout.addWidget(self.add_button)
        layout.addWidget(self.remove_button)
        layout.addWidget(navigation_buttons)
        #layout.addWidget(self.return_button)
        #layout.addWidget(self.continue_button)
        self.setLayout(layout)

    def add_flashcard(self):
        row_count = self.table.rowCount()
        self.table.insertRow(row_count)        

    def load_set_for_edit(self, flashcards_set):
        self.displayed_set = flashcards_set
        self.name_widget.name_line_edit.setText(flashcards_set.name)
        self.table.load_set_for_edit(flashcards_set)

    def get_flashcards_list(self):
        flashcards = []
        for row in range(self.table.rowCount()):
            original_item = self.table.item(row, 0)
            translation_item = self.table.item(row, 1)
            if original_item and translation_item:
                original_text = original_item.text()
                translation_text = translation_item.text()
                flashcards.append(Flashcard(original_text, translation_text))
        return flashcards

    def process_flashcards(self):
        new_set_name = self.name_widget.name_line_edit.text()
        self.controller.add_new_set(new_set_name, self.get_flashcards_list())
