from View.BasicTester.BasicFlashcardTester import BasicFlashcardTester
from View.BasicTester.BasicIncorrectWidget import IncorrectAnswer
from Database.DatabaseManager import DatabaseManager

class FlashcardsSetController:
    SET_ROLE = 100

    def __init__(self, db_manager: DatabaseManager) -> None:
        self.db_manager = db_manager

    def set_flashcards_widget(self, flashcards_widget):
        self.flashcards_widget = flashcards_widget

    def get_available_sets(self):
        return self.db_manager.get_all_sets()

    def show_create_set_view(self):
        self.flashcards_widget.stacked_layout.setCurrentWidget(self.flashcards_widget.create_sets_widget)

    def show_learn_view(self, flashcards_set):
        self.flashcards_widget.learn_set_widget.load_set_for_learning(flashcards_set)
        self.flashcards_widget.stacked_layout.setCurrentWidget(self.flashcards_widget.learn_set_widget)

    def show_test_view(self, flashcards_set):
        pass

    def create_set(self, new_set_name, flashcards):
        self.db_manager.create_new_flashcards_set(new_set_name, flashcards)
        self.flashcards_widget.stacked_layout.setCurrentWidget(self.flashcards_widget.show_sets_widget)

    def save_set(self, old_set_name, new_set_name, flashcards):
        self.db_manager.save_set(old_set_name, new_set_name, flashcards)
        self.return_from_set_editing()

    def show_set_details(self, flashcards_set):
        self.flashcards_widget.stacked_layout.setCurrentWidget(self.flashcards_widget.edit_sets_widget)
        self.flashcards_widget.edit_sets_widget.load_set_for_edit(flashcards_set)

    def is_valid_table_name(self, set_name):
        return self.db_manager.is_valid_table_name(set_name)

    def check_if_set_exists(self, set_name):
        return self.db_manager.check_if_set_exists(set_name)

    def return_from_set_editing(self):
        self.flashcards_widget.stacked_layout.setCurrentWidget(self.flashcards_widget.show_sets_widget)

    def return_from_set_creating(self):
        self.return_from_set_editing()

    def return_from_set_learning(self):
        self.return_from_set_editing()

    def remove_set(self, set_to_remove):
        if set_to_remove != None:
            self.db_manager.delete_flashcards_set(set_to_remove.name)
        self.return_from_set_editing()
