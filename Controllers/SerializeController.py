from Database.SerializeDatabaseManager import SerializeDatabaseManager
from configuration import get_serialize_db_manager
import pickle

class SerializeController:
    def __init__(self, db_manager: SerializeDatabaseManager = get_serialize_db_manager()) -> None:
        self.db_manager = db_manager

    def check_is_test_is_serialized(self, set_name):
        return self.db_manager.check_if_test_is_serialized(set_name)
    
    def get_serialized_test(self, set_name):
        serialized_test = self.db_manager.get_seralized_test(set_name)
        return pickle.loads(serialized_test)
    
    def serialize_test(self, set_name, test):
        serialized = pickle.dumps(test)
        self.db_manager.serialize_test(set_name, serialized)

    def delete_serialized_test(self, set_name):
        self.db_manager.delete_serialized_test(set_name)