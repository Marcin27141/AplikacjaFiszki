import os
import shutil
from CLI.Exporters.BaseExporter import BaseExporter
from Database.DatabaseManager import DatabaseManager
from CLI.FileOperator import FileOperator, FileAlias
from simple_app import get_default_db_manager

class SingleSetExporter(BaseExporter):
    def __init__(self, set_name, export_info) -> None:
        super().__init__(export_info)
        self.set_name = set_name
        self.set_to_export = self.get_set_by_name(self.set_name)
        self.name = self.name if self.name else self.get_default_set_filename(self.set_to_export)
    
    def export_set(self):
        self.export_set_to_textfile()

    def check_if_set_exists(self):
        return self.controller.check_if_set_exists(self.set_name)
    
    def get_set_by_name(self):
        return self.controller.get_set_by_name(self.set_name)
        
    def export_set_to_textfile(self):
        file_alias = FileAlias(self.destination_directory, self.destination_name)
        self.destination_name = self.FILE_OPERATOR.get_nonduplicate_filename(file_alias)
        set_text = self.get_set_to_text(self.set_to_export)
        file_alias = FileAlias(self.destination_directory, self.destination_name)
        self.FILE_OPERATOR.write_to_file(file_alias, set_text)