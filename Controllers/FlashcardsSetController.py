from Database.DatabaseManager import DatabaseManager
from configuration import get_db_manager

class FlashcardsSetController:
    SET_ROLE = 100

    def __init__(self, db_manager: DatabaseManager = get_db_manager()) -> None:
        self.db_manager = db_manager

    def get_available_sets(self):
        return self.db_manager.get_all_sets()
    
    def get_set_by_name(self, set_name):
        return self.db_manager.get_set_by_name(set_name)

    def create_set(self, new_set_name, flashcards):
        self.db_manager.create_new_flashcards_set(new_set_name, flashcards)

    def save_set(self, old_set_name, new_set_name, flashcards):
        self.db_manager.save_set(old_set_name, new_set_name, flashcards)

    def update_set_statistics(self, flashcards_set):
        self.db_manager.save_set(flashcards_set.name, flashcards_set.name, flashcards_set.flashcards)

    def is_valid_set_name(self, set_name):
        return self.db_manager.is_valid_table_name(set_name)

    def check_if_set_exists(self, set_name):
        return self.db_manager.check_if_set_exists(set_name)

    def remove_set(self, set_to_remove):
        if set_to_remove != None:
            self.remove_set_by_name(set_to_remove.name)

    def remove_set_by_name(self, set_name):
        if set_name != None:
            self.db_manager.delete_flashcards_set(set_name)
