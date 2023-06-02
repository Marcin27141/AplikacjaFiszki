import os

class FileAlias:
    def __init__(self, directory, filename) -> None:
        self.directory = directory
        self.filename = filename

class FileOperator:
    DEFAULT_ENCODING = 'utf-8'

    def check_if_file_exists(self, filepath):
        return os.path.isfile(filepath)

    def check_if_directory_exists(self, directory):
        return os.path.isdir(directory)

    def get_path(self, file_alias):
        return os.path.join(file_alias.directory, file_alias.filename)

    def create_directory(self, dir_name):
        os.makedirs(dir_name)

    def write_to_file(self, file_alias, input):
        path = self.get_path(file_alias)
        self.__write_to_file(path, input)

    def __write_to_file(self, filepath, input):
        with open(filepath, "w", encoding=self.DEFAULT_ENCODING) as file:
            file.write(input)

    def get_nonduplicate_filename(self, file_alias):
        DEFAULT_APPEND = '_copy'
        if self.check_if_file_exists(self.get_path(file_alias)):
            file_alias.filename = file_alias.filename+DEFAULT_APPEND
        return file_alias.filename