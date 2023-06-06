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
    
    def get_path_with_extension(self, file_alias, extension):
        extension_append = "" if not extension else f".{extension}"
        return os.path.join(file_alias.directory, f"{file_alias.filename}{extension_append}")

    def create_directory(self, dir_name):
        os.makedirs(dir_name)

    def write_to_file(self, file_alias, input):
        path = self.get_path(file_alias)
        self.__write_to_file(path, input)

    def __write_to_file(self, filepath, input):
        with open(filepath, "w", encoding=self.DEFAULT_ENCODING) as file:
            file.write(input)

    def get_nonduplicate_filename(self, file_alias, extension = None):
        def get_iteration_filename(filename):
            idx = 1
            original_filename = file_alias.filename
            while self.check_if_file_exists(self.get_path_with_extension(file_alias, extension)):
                file_alias.filename = f"{original_filename}({idx})"
                idx += 1   
            return file_alias.filename
        return get_iteration_filename(file_alias.filename)