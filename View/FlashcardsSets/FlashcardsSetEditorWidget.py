from PySide6.QtWidgets import QWidget, QTableWidget, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox
from PySide6.QtCore import Qt, Signal
from View.FlashcardsSets.FlashcardsSetEditTable import FlashcardSetEditTable
from View.FlashcardsSets.NameWidget import NameWidget
from View.TimeTester.TimeTestWidget import TimeTestWidget
from Model.Flashcards import Flashcard
from View.ViewUtilities import set_widget_font_size

class FlashcardsSetEditorWidget(QWidget):
    RETURN_TO_MENU = Signal()
    SHOW_LEARN_VIEW = Signal(object)
    SHOW_TEST_VIEW = Signal(object)
    SHOW_TIME_TEST_VIEW = Signal(object)
    
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.name_widget = NameWidget()
        set_widget_font_size(self.name_widget, 15)

        self.learn_button = QPushButton("Learn")
        self.learn_button.clicked.connect(lambda: self.SHOW_LEARN_VIEW.emit(self.displayed_set))
        self.test_button = QPushButton("Test")
        self.test_button.clicked.connect(lambda: self.test_button_clicked())

        activity_buttons = QWidget()
        activity_layout = QHBoxLayout()
        activity_layout.addWidget(self.learn_button)
        activity_layout.addWidget(self.test_button)
        activity_buttons.setLayout(activity_layout)

        self.table = FlashcardSetEditTable()
        
        self.add_button = QPushButton("Add Flashcard")
        self.add_button.clicked.connect(lambda: self.add_flashcard())

        self.remove_button = QPushButton("Remove set")
        self.remove_button.setStyleSheet("background-color: red; color: white")
        self.remove_button.clicked.connect(self.remove_set)

        self.return_button = QPushButton("Return")
        self.return_button.clicked.connect(lambda: self.RETURN_TO_MENU.emit())

        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(lambda: self.process_flashcards())

        navigation_buttons = QWidget()
        navigation_layout = QHBoxLayout()
        navigation_layout.addWidget(self.return_button)
        navigation_layout.addWidget(self.save_button)
        navigation_buttons.setLayout(navigation_layout)

        self.error_label = QLabel()
        self.error_label.setStyleSheet("color: red;")

        layout = QVBoxLayout()
        layout.addWidget(self.name_widget)
        layout.addWidget(activity_buttons)
        layout.addWidget(self.table)
        layout.addWidget(self.add_button)
        layout.addWidget(self.remove_button)
        layout.addWidget(navigation_buttons)
        layout.addWidget(self.error_label)
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
    
    def get_test_message_box(self):
        test_kind_message_box = QMessageBox(self)
        test_kind_message_box.setWindowTitle("Choose test kind")
        test_kind_message_box.setText("What type of test do you want to take?")
        test_kind_message_box.addButton("Normal test", QMessageBox.ButtonRole.YesRole)
        test_kind_message_box.addButton("Time test", QMessageBox.ButtonRole.NoRole)    
        return test_kind_message_box
    
    def get_time_test_unavailable_message_box(self):
        time_test_unavailable_message_box = QMessageBox(self)
        time_test_unavailable_message_box.setWindowTitle("Time test unavailable")
        time_test_unavailable_message_box.setText(f"Time test is unavailable for this set.\nMinimum number of flashcards in a set is {TimeTestWidget.NUM_OF_POSSIBILITIES}")
        time_test_unavailable_message_box.setStandardButtons(QMessageBox.Ok)
        return time_test_unavailable_message_box

    def test_button_clicked(self):
        def set_is_eligible_for_time_test(flashcards_set):
            return len(flashcards_set.flashcards) >= TimeTestWidget.NUM_OF_POSSIBILITIES
        test_kind_message_box = self.get_test_message_box()
        clicked_button = test_kind_message_box.exec()
        NORMAL_TEST_CHOSEN = 0
        TIME_TEST_CHOSEN = 1
        if clicked_button == NORMAL_TEST_CHOSEN:
            self.switch_to_test_widget()
        elif clicked_button == TIME_TEST_CHOSEN and set_is_eligible_for_time_test(self.displayed_set):
            self.SHOW_TIME_TEST_VIEW.emit(self.displayed_set)
        elif clicked_button == TIME_TEST_CHOSEN:
            time_test_information_box = self.get_time_test_unavailable_message_box()
            time_test_information_box.exec()

    def switch_to_test_widget(self):
        self.SHOW_TEST_VIEW.emit(self.displayed_set)

    def remove_set(self):
        question = QMessageBox.question(self, "Delete Set", "Are you sure you want to delete this set?",
                                              QMessageBox.Yes | QMessageBox.No)
        if question == QMessageBox.Yes:
            self.controller.remove_set(self.displayed_set)
            self.RETURN_TO_MENU.emit()

    def process_flashcards(self):
        set_name = self.name_widget.name_line_edit.text()
        if not len(set_name) > 0:
            self.error_label.setText("Name of the set is mandatory")
        elif not self.controller.is_valid_set_name(set_name):
            self.error_label.setText("This set name is not valid")
        elif set_name != self.displayed_set.name and self.controller.check_if_set_exists(set_name):
            self.error_label.setText("Set with given name already exists")
        else:
            self.controller.save_set(self.displayed_set.name, set_name, self.get_flashcards_list())
            self.RETURN_TO_MENU.emit()   

    def showEvent(self, event):
        super().showEvent(event)
        self.name_widget.name_line_edit.clear()
        self.table.clearContents()
        self.table.setRowCount(1)
        self.error_label.clear()
