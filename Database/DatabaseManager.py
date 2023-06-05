import sqlite3
from Model.Flashcards import StatsFlashcard
from Model.FlashcardsSet import FlashcardsSet
from Database.GeneralDatabaseManager import GeneralDatabaseManager

class DatabaseManager(GeneralDatabaseManager):
    def __init__(self, db_name) -> None:
        super().__init__(db_name)
        self.initialize_database()

    def initialize_database(self):
        conn, cursor = self.get_database_connection_and_cursor()
        if not self.check_if_table_exists("Flashcards", cursor):
            self.create_table("Flashcards", cursor)
            conn.commit()
            initial_flashcards = [StatsFlashcard("kot", "cat"), StatsFlashcard("pies", "dog"), StatsFlashcard("krowa", "cow"), StatsFlashcard("koń", "horse")]
            self.populate_flashcards(cursor, "Flashcards", initial_flashcards)
            conn.commit()
        conn.close()

    def create_table(self, name, cursor):
        cursor.execute(f"""CREATE TABLE {name}
                        (id INTEGER PRIMARY KEY,
                        original TEXT NOT NULL,
                        translation TEXT NOT NULL,
                        times_correct INTEGER,
                        times_incorrect INTEGER,
                        last_tested DATETIME)""")

    def check_if_set_exists(self, set_name):
        conn, cursor = self.get_database_connection_and_cursor()
        result = self.check_if_table_exists(set_name, cursor)
        conn.close()
        return result
        
    def get_all_sets(self):
        conn, cursor = self.get_database_connection_and_cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        table_names = cursor.fetchall()
        flashcard_sets = []
        for table_name in table_names:
            flashcard_sets.append(self.get_set(table_name[0], cursor))
        conn.close()
        return flashcard_sets
    
    def get_set_by_name(self, set_name):
        conn, cursor = self.get_database_connection_and_cursor()
        result = self.get_set(set_name, cursor)
        conn.close()
        return result

    def get_set(self, set_name, cursor):
        cursor.execute(f'SELECT * FROM {set_name}')
        flashcards = []
        for (key, original, translation, times_correct, times_incorrect, last_tested) in cursor.fetchall():
            flashcards.append(StatsFlashcard(original, translation, times_correct, times_incorrect, last_tested))
        return FlashcardsSet(set_name, flashcards)

    def create_new_flashcards_set(self, name, flashcards):
        conn, cursor = self.get_database_connection_and_cursor()
        if self.check_if_table_exists(name, cursor):
            raise Exception("Set with given name already exists")
        self.create_table(name, cursor)
        self.populate_flashcards(cursor, name, flashcards)
        conn.commit()
        conn.close()

    def save_set(self, old_set_name, new_set_name, flashcards):
        conn, cursor = self.get_database_connection_and_cursor()
        if not self.check_if_table_exists(old_set_name, cursor):
            raise Exception(f"table {old_set_name} doesn't exist")
        else:
            self.clear_table_contents(old_set_name)
            self.populate_flashcards(cursor, old_set_name, flashcards)
            conn.commit()
            if old_set_name != new_set_name: self.rename_set(old_set_name, new_set_name, cursor)
        conn.commit()
        conn.close()

    def rename_set(self, old_set_name, new_set_name, cursor):
        self.rename_table(old_set_name, new_set_name, cursor)

    def delete_flashcards_set(self, set_name):
        self.delete_table(set_name)
        
    def populate_flashcards(self, cursor, table_name, flashcards):
        flashcards_tuples = []
        for flashcard in flashcards:
            flashcards_tuples.append((flashcard.original, flashcard.translation, flashcard.times_correct, flashcard.times_incorrect, flashcard.last_tested))
        cursor.executemany(f"INSERT INTO {table_name} (original, translation, times_correct, times_incorrect, last_tested) VALUES (?,?,?,?,?)", flashcards_tuples)