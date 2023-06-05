import sqlite3

class GeneralDatabaseManager:
    def __init__(self, db_name) -> None:
        self.database_name = db_name

    def get_database_connection_and_cursor(self):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        return conn, cursor

    def is_valid_table_name(self, name):
        if not name: return False
        if not (name[0].isalpha() or name[0] == '_'): return False

        valid_chars = set("_$")
        for char in name[1:]:
            if not (char.isalnum() or char in valid_chars):
                return False
        return True

    def check_if_table_exists(self, table_name, cursor):
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
        result = cursor.fetchone()
        return bool(result)

    def rename_table(self, old_table_name, new_table_name, cursor):
        cursor.execute(f"ALTER TABLE {old_table_name} RENAME TO {new_table_name}")

    def delete_table(self, table_name):
        conn, cursor = self.get_database_connection_and_cursor()
        cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
        conn.commit()
        conn.close()

    def clear_table_contents(self, table_name):
        conn, cursor = self.get_database_connection_and_cursor()
        cursor.execute(f"DELETE FROM {table_name}")
        conn.commit()
        conn.close()