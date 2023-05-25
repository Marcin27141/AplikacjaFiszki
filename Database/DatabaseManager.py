import sqlite3

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
            self.create_flashcards_table(cursor)
            conn.commit()
            self.populate_initial_flashcards(cursor)
            conn.commit()
        conn.close()

    def check_if_table_exists(self, table_name, cursor):
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
        result = cursor.fetchone()
        return bool(result)
    
    def create_flashcards_table(self, cursor):
        cursor.execute("""CREATE TABLE Flashcards
                        (id INTEGER PRIMARY KEY,
                        original TEXT NOT NULL,
                        translation TEXT NOT NULL)""")
        
    def populate_initial_flashcards(self, cursor):
        initial_flashcards = [("kot", "cat"), ("pies", "dog"), ("krowa", "cow"), ("koń", "horse")]
        cursor.executemany("INSERT INTO Flashcards (original, translation) VALUES (?, ?)", initial_flashcards)