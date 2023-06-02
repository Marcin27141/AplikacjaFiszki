from Controllers.FlashcardsSetController import FlashcardsSetController
from CLI.FileOperator import FileOperator

class ExportInfo:
    def __init__(self, destination_dir, destination_name, separator) -> None:
        self.destination_dir = destination_dir
        self.destination_name = destination_name
        self.separator = separator

class BaseExporter:
    FILE_OPERATOR = FileOperator()
    DEFAULT_SEPARATOR = ' - '

    def __init__(self, export_info) -> None:
        self.controller = FlashcardsSetController()
        self.destination_directory = export_info.destination_dir
        self.name = export_info.destination_name
        self.separator = export_info.separator if export_info.separator else self.DEFAULT_SEPARATOR
    
    def get_default_set_filename(self, flashcards_set):
        return f'{flashcards_set.name}.txt'
    
    def check_if_directory_exists(self):
        return self.FILE_OPERATOR.check_if_directory_exists(self.destination_directory)
    
    def get_set_to_text(self, flashcards_set):
        result = []
        for flashcard in flashcards_set.flashcards:
            result.append(f"{flashcard.original}{self.separator}{flashcard.translation}")
        return '\n'.join(result)