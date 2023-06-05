from Database.DatabaseManager import DatabaseManager
from Database.SerializeDatabaseManager import SerializeDatabaseManager

DATABASE_NAME = 'flashcards_database.db'
SERIALIZE_DATABASE_NAME = 'serialization_database.db'

def get_db_manager():
    return DatabaseManager(DATABASE_NAME)

def get_serialize_db_manager():
    return SerializeDatabaseManager(SERIALIZE_DATABASE_NAME)