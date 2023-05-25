from View.BasicTester.BasicFlashcardTester import BasicFlashcardTester
from View.BasicTester.BasicIncorrectWidget import IncorrectAnswer
from Database.DatabaseManager import DatabaseManager

class SetEditorController:
    def __init__(self, db_manager: DatabaseManager) -> None:
        self.db_manager = db_manager

    def set_editor_widget(self, editor_widget):
        self.editor_widget = editor_widget

    def add_new_set(self, new_set_name, flashcards):
        self.db_manager.create_new_flashcards_set(new_set_name, flashcards)