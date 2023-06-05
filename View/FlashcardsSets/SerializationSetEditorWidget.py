from PySide6.QtWidgets import QWidget, QTableWidget, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox
from PySide6.QtCore import Qt, Signal
from View.FlashcardsSets.FlashcardsSetEditorWidget import FlashcardsSetEditorWidget

class SerializationSetEditorWidget(FlashcardsSetEditorWidget):
    LOAD_SERIALIZED_TEST = Signal(object)

    def __init__(self, controller, serialize_controller):
        super().__init__(controller)
        self.serialize_controller = serialize_controller

    def get_serialized_test_message_box(self):
        return QMessageBox.question(self, "Load test", "There is an unfinished test for this set.\nDo you want to continue?",
                                              QMessageBox.Yes | QMessageBox.No)

    def switch_to_test_widget(self):
        if self.serialize_controller.check_is_test_is_serialized(self.displayed_set.name):
            serialized_test_box = self.get_serialized_test_message_box()
            if serialized_test_box == QMessageBox.Yes:
                serialized_test = self.get_serialized_test()
                self.LOAD_SERIALIZED_TEST.emit(serialized_test)
            elif serialized_test_box == QMessageBox.No:
                super().switch_to_test_widget()
            self.delete_serialized_test()
        else: super().switch_to_test_widget()

    def get_serialized_test(self):
        return self.serialize_controller.get_serialized_test(self.displayed_set.name)
    
    def delete_serialized_test(self):
        self.serialize_controller.delete_serialized_test(self.displayed_set.name)
