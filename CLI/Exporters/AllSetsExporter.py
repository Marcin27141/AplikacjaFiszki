import os
import shutil
from CLI.Exporters.BaseExporter import BaseExporter
from Database.DatabaseManager import DatabaseManager
from CLI.FileOperator import FileOperator, FileAlias
from simple_app import get_default_db_manager
from datetime import datetime

class AllSetsExporter(BaseExporter):
    def __init__(self, export_info) -> None:
        super().__init__(export_info)
        self.name = self.name if self.name else self.get_default_archive_name()

    def export_sets(self):
        self.export_all_sets_to_archive()

    def get_all_sets(self):
        return self.db_manager.get_all_sets()

    def create_temporary_directory(self):
        TEMP_DIRECTORY = "temp_directory"
        self.FILE_OPERATOR.create_directory(TEMP_DIRECTORY)
        return TEMP_DIRECTORY        

    def get_content_directory_for_archive(self):
        temp_directory = self.create_temporary_directory()
        for flashcards_set in self.sets_to_export:
            filename = self.get_default_set_filename(flashcards_set)
            set_text = self.get_set_to_text(flashcards_set)
            file_alias = FileAlias(temp_directory, filename)
            self.FILE_OPERATOR.write_to_file(file_alias, set_text)
        
    def export_all_sets_to_archive(self):
        DEFAULT_ARCHIVE_FORMAT = 'zip'
        file_alias = FileAlias(self.destination_directory, self.destination_name)
        self.destination_name = self.FILE_OPERATOR.get_nonduplicate_filename(file_alias)
        content_directory_for_archive = self.get_content_directory_for_archive()
        shutil.make_archive(self.destination_name, DEFAULT_ARCHIVE_FORMAT, content_directory_for_archive)
        shutil.rmtree(content_directory_for_archive)

    def get_default_archive_name(self):
        return f'CreatedSets_{datetime.now()}'