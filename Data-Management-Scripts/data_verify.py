import sqlite3
import sys

class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_name)
        except sqlite3.Error as e:
            print("Error connecting to the database:", e)

    def execute_query(self, query, params=None):
        if not self.connection:
            print("Database connection is not established.")
            return []

        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return cursor.fetchall()
        except sqlite3.Error as e:
            print("Error executing query:", e)
            return []

    def close_connection(self):
        if self.connection:
            self.connection.close()
            self.connection = None

def main():
    try:
        db_manager = DatabaseManager("users.db")
        db_manager.connect()
        
        records = db_manager.execute_query("SELECT * FROM Records")
        if records:
            for record in records:
                print(record)
        else:
            print("No records found.")
    except KeyboardInterrupt:
            print("Process interrupted by the user.")
            sys.exit(1)
    except Exception as e:
            print(f"An unexpected error occurred: {e}")
            sys.exit(1)
    finally:
        if db_manager:
            db_manager.close_connection()

if __name__ == "__main__":
    main()
    sys.exit(0)