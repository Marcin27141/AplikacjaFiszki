import os
from Controllers.FlashcardsSetController import FlashcardsSetController
from Database.DatabaseManager import DatabaseManager
from Model.Flashcards import Flashcard

DATABASE_NAME = 'flashcards_database.db'
db_manager = DatabaseManager(DATABASE_NAME)
FLASHCARDS_CONTROLLER = FlashcardsSetController(db_manager)

def check_if_file_exists(file):
    return os.path.isfile(file)

def check_if_name_is_valid(name):
    return FLASHCARDS_CONTROLLER.is_valid_table_name(name)

def check_if_set_exists(name):
    return FLASHCARDS_CONTROLLER.check_if_set_exists(name)

def create_set(name, flashcards):
    FLASHCARDS_CONTROLLER.create_set(name, flashcards)

def convert_text_to_flashcards(text, separator):
    with open(text, 'r', encoding='utf-8') as file:
        result = []
        for line in file:
            (original, translation) = line.split(separator)
            result.append(Flashcard(original.strip(), translation.strip()))
        return result