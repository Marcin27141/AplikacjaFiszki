from Database.DatabaseManager import DatabaseManager

DATABASE_NAME = 'flashcards_database.db'

def get_db_manager():
    return DatabaseManager(DATABASE_NAME)