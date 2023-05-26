import sqlite3
from Model.Flashcards import Flashcard
from Model.FlashcardsSet import FlashcardsSet

class DatabaseManager:
    def __init__(self, db_name) -> None:
        self.database_name = db_name

    def get_database_connection_and_cursor(self):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        return conn, cursor

    def initialize_database(self):
        conn, cursor = self.get_database_connection_and_cursor()
        if not self.check_if_table_exists("Flashcards", cursor):
            self.create_table("Flashcards", cursor)
            conn.commit()
            initial_flashcards = [("kot", "cat"), ("pies", "dog"), ("krowa", "cow"), ("koń", "horse")]
            self.populate_flashcards(cursor, "Flashcards", initial_flashcards)
            conn.commit()
        conn.close()

    def check_if_table_exists(self, table_name, cursor):
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
        result = cursor.fetchone()
        return bool(result)
    
    def create_table(self, name, cursor):
        cursor.execute(f"""CREATE TABLE {name}
                        (id INTEGER PRIMARY KEY,
                        original TEXT NOT NULL,
                        translation TEXT NOT NULL)""")
        
    def get_all_sets(self):
        conn, cursor = self.get_database_connection_and_cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        table_names = cursor.fetchall()
        flashcard_sets = []
        for table_name in table_names:
            cursor.execute(f"SELECT * FROM {table_name[0]}")
            flashcards = [Flashcard(original, translation) for (key, original, translation) in cursor.fetchall()]
            flashcard_set = FlashcardsSet(table_name[0], flashcards)
            flashcard_sets.append(flashcard_set)
        conn.close()
        return flashcard_sets


    def create_new_flashcards_set(self, name, flashcards):
        conn, cursor = self.get_database_connection_and_cursor()
        if self.check_if_table_exists(name, cursor):
            raise Exception("Set with given name already exists")
        self.create_table(name, cursor)
        self.populate_flashcards(cursor, name, flashcards)
        conn.close()
        
    def populate_flashcards(self, cursor, table_name, flashcards):
        flashcards_tuples = [(flashcard.original, flashcard.translation) for flashcard in flashcards]
        cursor.executemany(f"INSERT INTO {table_name} (original, translation) VALUES (?, ?)", flashcards_tuples)