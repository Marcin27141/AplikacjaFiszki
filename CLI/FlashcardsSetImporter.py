from Controllers.FlashcardsSetController import FlashcardsSetController
from Database.DatabaseManager import DatabaseManager
from Model.Flashcards import Flashcard
from simple_app import DATABASE_NAME
from CLI.FileOperator import FileOperator, FileAlias
from simple_app import get_default_db_manager

class WrongFileFormatException(Exception):
    "File was not formatted properly"

class ImportInfo:
    def __init__(self, filepath, name, separator) -> None:
        self.filepath = filepath
        self.set_name = name
        self.separator = separator

class FlashcardsSetImporter:
    FILE_OPERATOR = FileOperator()

    def __init__(self, import_info) -> None:
        self.controller = FlashcardsSetController()
        self.db_manager: DatabaseManager = get_default_db_manager()
        self.filepath = import_info.filepath
        self.set_name = import_info.set_name
        self.separator = import_info.separator

    def import_set(self):
        flashcards = self.get_flashcards_from_file()
        self.create_set(flashcards)

    def check_if_file_exists(self):
        return self.FILE_OPERATOR.check_if_file_exists(self.filepath)
    
    def check_if_name_is_valid(self):
        return self.controller.is_valid_set_name(self.set_name)

    def check_if_set_exists(self):
        return self.controller.check_if_set_exists(self.set_name)

    def get_flashcards_from_file(self):
        DEFAULT_ENCODING = 'zip'
        with open(self.filepath, 'r', encoding=DEFAULT_ENCODING) as file_text:
                return self.convert_text_to_flashcards(file_text)

    def convert_text_to_flashcards(self, text):
        result = []
        for line in text:
            flashcard = self.convert_line_to_flashcard(line)
            result.append(flashcard)
        return result
            
    def convert_line_to_flashcard(self, line):
        (original, translation) = line.split(self.separator)
        return Flashcard(original.strip(), translation.strip())
    
    def create_set(self, flashcards):
        self.controller.create_set(self.set_name, flashcards)