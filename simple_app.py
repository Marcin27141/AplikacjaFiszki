from Model.Flashcards import Flashcard
from View.BasicView import StartView
from Database.DatabaseManager import DatabaseManager

"""flashcards = [
    Flashcard("kot", "cat"),
    Flashcard("pies", "dog"),
    Flashcard("krowa", "cow"),
    Flashcard("koń", "horse"),
    Flashcard("osioł", "donkey"),
    Flashcard("kura", "hen"),
]"""

DATABASE_NAME = 'flashcards_database.db'
db_manager = DatabaseManager(DATABASE_NAME)
db_manager.initialize_database()

def get_initial_flashcards():
    conn, cursor = db_manager.get_database_connection_and_cursor()
    cursor.execute("SELECT * FROM Flashcards")
    rows = cursor.fetchall()
    conn.close()
    return [Flashcard(original, translation) for (key, original, translation) in rows]

conn, cursor = db_manager.get_database_connection_and_cursor()
initial_flashcards = get_initial_flashcards()

start_view = StartView(initial_flashcards)
start_view.show()