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

    def is_valid_table_name(self, name):
        if not name: return False
        if not (name[0].isalpha() or name[0] == '_'): return False

        valid_chars = set("_$")
        for char in name[1:]:
            if not (char.isalnum() or char in valid_chars):
                return False
        return True

    def check_if_set_exists(self, set_name):
        conn, cursor = self.get_database_connection_and_cursor()
        result = self.check_if_table_exists(set_name, cursor)
        conn.close()
        return result

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
            flashcard_sets.append(self.get_set(table_name[0], cursor))
        conn.close()
        return flashcard_sets
    
    def get_set(self, set_name, cursor):
        cursor.execute(f'SELECT * FROM {set_name}')
        flashcards = [Flashcard(original, translation) for (key, original, translation) in cursor.fetchall()]
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
        cursor.execute(f"ALTER TABLE {old_set_name} RENAME TO {new_set_name}")

    def delete_flashcards_set(self, set_name):
        conn, cursor = self.get_database_connection_and_cursor()
        cursor.execute(f"DROP TABLE IF EXISTS {set_name}")
        conn.commit()
        conn.close()
        
    def populate_flashcards(self, cursor, table_name, flashcards):
        flashcards_tuples = [(flashcard.original, flashcard.translation) for flashcard in flashcards]
        cursor.executemany(f"INSERT INTO {table_name} (original, translation) VALUES (?, ?)", flashcards_tuples)

    def clear_table_contents(self, table_name):
        conn, cursor = self.get_database_connection_and_cursor()
        cursor.execute(f"DELETE FROM {table_name}")
        conn.commit()
        conn.close()