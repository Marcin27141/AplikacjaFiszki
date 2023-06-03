from PySide6.QtWidgets import QWidget, QTableWidget, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit
from PySide6.QtCore import Qt, Signal
from View.FlashcardsSets.FlashcardsSetEditTable import FlashcardSetEditTable
from View.FlashcardsSets.NameWidget import NameWidget
from Model.Flashcards import Flashcard
from View.ViewUtilities import set_widget_font_size, make_font_bold

class FlashcardsSetCreatorWidget(QWidget):
    RETURN_TO_MENU = Signal()
    
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.name_widget = NameWidget()
        set_widget_font_size(self.name_widget, 15)

        self.table = FlashcardSetEditTable()
        
        self.add_button = QPushButton("Add Flashcard")
        self.add_button.clicked.connect(lambda: self.add_flashcard())

        self.return_button = QPushButton("Return")
        self.return_button.clicked.connect(lambda: self.RETURN_TO_MENU.emit())

        self.create_button = QPushButton("Create")
        self.create_button.clicked.connect(lambda: self.process_flashcards())

        navigation_buttons = QWidget()
        navigation_layout = QHBoxLayout()
        navigation_layout.addWidget(self.return_button)
        navigation_layout.addWidget(self.create_button)
        navigation_buttons.setLayout(navigation_layout)

        self.error_label = QLabel()
        self.error_label.setStyleSheet("color: red;")
        make_font_bold(self.error_label)
        self.error_label.setAlignment(Qt.AlignHCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.name_widget)
        layout.addWidget(self.table)
        layout.addWidget(self.add_button)
        layout.addWidget(navigation_buttons)
        layout.addWidget(self.error_label)
        self.setLayout(layout)

    def add_flashcard(self):
        row_count = self.table.rowCount()
        #self.table.insertRow(row_count)        
        self.table.add_row_with_edit(row_count)

    def get_flashcards_list(self):
        flashcards = []
        for row in range(self.table.rowCount()):
            original_item = self.table.item(row, 0)
            translation_item = self.table.item(row, 1)
            if self.table.check_if_row_is_filled(row):
                original_text = original_item.text()
                translation_text = translation_item.text()
                flashcards.append(Flashcard(original_text, translation_text))
        return flashcards

    def process_flashcards(self):
        set_name = self.name_widget.name_line_edit.text()
        if not len(set_name) > 0:
            self.error_label.setText("Name of the set is mandatory")
        elif not self.controller.is_valid_set_name(set_name):
            self.error_label.setText("This set name is not valid")
        elif self.controller.check_if_set_exists(set_name):
            self.error_label.setText("Set with given name already exists")
        elif not self.table.check_if_no_partially_filled_rows():
            self.error_label.setText("Please fill all non-empty rows")
        else:
            self.controller.create_set(set_name, self.get_flashcards_list())
            self.RETURN_TO_MENU.emit()

    def showEvent(self, event):
        super().showEvent(event)
        self.name_widget.name_line_edit.clear()
        self.table.clearContents()
        self.table.setRowCount(1)
        self.error_label.clear()