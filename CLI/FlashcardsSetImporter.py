from Controllers.FlashcardsSetController import FlashcardsSetController
from Model.Flashcards import StatsFlashcard
from CLI.FileOperator import FileOperator

class WrongFileFormatException(Exception):
    "File was not formatted properly"

class ImportInfo:
    def __init__(self, filepath, name, separator, is_reverse) -> None:
        self.filepath = filepath
        self.set_name = name
        self.separator = separator
        self.is_reverse = is_reverse

class FlashcardsSetImporter:
    FILE_OPERATOR = FileOperator()

    def __init__(self, import_info) -> None:
        self.controller = FlashcardsSetController()
        self.filepath = import_info.filepath
        self.set_name = import_info.set_name
        self.separator = import_info.separator
        self.is_reverse = import_info.is_reverse

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
        DEFAULT_ENCODING = 'utf-8'
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
        if self.is_reverse: (original, translation) = (translation, original)
        return StatsFlashcard(original.strip(), translation.strip())
    
    def create_set(self, flashcards):
        self.controller.create_set(self.set_name, flashcards)