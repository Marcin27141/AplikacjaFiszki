import os
import shutil
from Controllers.FlashcardsSetController import FlashcardsSetController
from Database.DatabaseManager import DatabaseManager
from Model.Flashcards import Flashcard

DATABASE_NAME = 'flashcards_database.db'
db_manager = DatabaseManager(DATABASE_NAME)
FLASHCARDS_CONTROLLER = FlashcardsSetController(db_manager)

def check_if_file_exists(file):
    return os.path.isfile(file)

def check_if_directory_exists(directory):
    return os.path.isdir(directory)

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
    
def get_set_to_text(set_name, separator):
    flashcard_set = db_manager.get_set_by_name(set_name)
    result = []
    for flashcard in flashcard_set.flashcards:
        result.append(f"{flashcard.original}{separator}{flashcard.translation}")
    return '\n'.join(result)

def write_set_text_to_file(set_text, directory, name):
    if check_if_file_exists(os.path.join(directory, name)): name = name+"_copy"
    filepath = os.path.join(directory, name)
    with open(filepath, "w", encoding='utf-8') as file:
        file.write(set_text)

def export_all_sets_to_archive(directory, name, separator):
    temp_directory = "temp_directory"
    os.makedirs(temp_directory)
    if check_if_file_exists(os.path.join(directory, name)): name = name+"_copy"
    filepath = os.path.join(directory, name)
    all_sets = db_manager.get_all_sets()
    for index, flashcards_set in enumerate(all_sets):
        filename = f'{flashcards_set.name}.txt'
        set_text = get_set_to_text(flashcards_set.name, separator)
        write_set_text_to_file(set_text, temp_directory, filename)
    shutil.make_archive(name, 'zip', temp_directory)  # Create the archive
    shutil.rmtree(temp_directory)
