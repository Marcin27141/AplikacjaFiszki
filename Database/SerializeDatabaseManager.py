import sqlite3
from Model.Flashcards import Flashcard
from Model.FlashcardsSet import FlashcardsSet
from Database.GeneralDatabaseManager import GeneralDatabaseManager

class SerializeDatabaseManager(GeneralDatabaseManager):
    SERIALIZED_TESTS_TABLE = 'SerializedTests'

    def __init__(self, db_name) -> None:
        super().__init__(db_name)
        self.initialize_database()

    def initialize_database(self):
        conn, cursor = self.get_database_connection_and_cursor()
        if not self.check_if_table_exists(self.SERIALIZED_TESTS_TABLE, cursor):
            self.create_table(self.SERIALIZED_TESTS_TABLE, cursor)
            conn.commit()
        conn.close()

    def create_table(self, name, cursor):
        cursor.execute(f'CREATE TABLE {self.SERIALIZED_TESTS_TABLE} (id INTEGER PRIMARY KEY, set_name TEXT NOT NULL, serialized BLOB)')

    def check_if_test_is_serialized(self, set_name):
        return self.get_seralized_test(set_name) != None
    
    def get_seralized_test(self, set_name):
        conn, cursor = self.get_database_connection_and_cursor()
        query = f"SELECT * FROM {self.SERIALIZED_TESTS_TABLE} WHERE set_name=?"
        cursor.execute(query, (set_name,))
        result = cursor.fetchone()
        conn.close()
        if not result: return result
        else:
            (_, _, serialized_test) = result
            return serialized_test

    def serialize_test(self, set_name, serialized):
        conn, cursor = self.get_database_connection_and_cursor()
        cursor.execute(f"INSERT INTO {self.SERIALIZED_TESTS_TABLE} (set_name, serialized) VALUES (?, ?)", (set_name, serialized))
        conn.commit()
        conn.close()

    def delete_serialized_test(self, set_name):
        conn, cursor = self.get_database_connection_and_cursor()
        query = f"DELETE FROM {self.SERIALIZED_TESTS_TABLE} WHERE set_name = ?"
        cursor.execute(query, (set_name, ))
        conn.commit()
        conn.close()