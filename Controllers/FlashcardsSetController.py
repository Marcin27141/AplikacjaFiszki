from Database.DatabaseManager import DatabaseManager
from simple_app import get_default_db_manager

class FlashcardsSetController:
    def __init__(self, db_manager: DatabaseManager = get_default_db_manager()) -> None:
        self.db_manager = db_manager

    def get_available_sets(self):
        return self.db_manager.get_all_sets()
    
    def get_set_by_name(self, set_name):
        return self.db_manager.get_set_by_name(set_name)

    def create_set(self, new_set_name, flashcards):
        self.db_manager.create_new_flashcards_set(new_set_name, flashcards)

    def save_set(self, old_set_name, new_set_name, flashcards):
        self.db_manager.save_set(old_set_name, new_set_name, flashcards)    

    def is_valid_set_name(self, set_name):
        return self.db_manager.is_valid_table_name(set_name)

    def check_if_set_exists(self, set_name):
        return self.db_manager.check_if_set_exists(set_name)

    def remove_set(self, set_to_remove):
        if set_to_remove != None:
            self.db_manager.delete_flashcards_set(set_to_remove.name)
