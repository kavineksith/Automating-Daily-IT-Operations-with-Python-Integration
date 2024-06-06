import os
import sys
import csv
import sqlite3
from pathlib import Path

class DatabaseManager:
    def __init__(self, source_file):
        self.source_file = source_file

    def create_database(self):
        try:
            connection = sqlite3.connect("users.db")
            cursor = connection.cursor()
            table_query = "CREATE TABLE IF NOT EXISTS UserInformation (UserID INTEGER PRIMARY KEY AUTOINCREMENT, FirstName TEXT NOT NULL, LastName TEXT NOT NULL, EmailAddress TEXT NOT NULL)"
            cursor.execute(table_query)
            connection.commit()
            return connection, cursor
        except sqlite3.Error as e:
            print("Error creating database:", e)
            sys.exit(1)

    def insert_data(self, cursor, row):
        try:
            insert_query = "INSERT INTO UserInformation (FirstName, LastName, EmailAddress) VALUES (?, ?, ?)"
            cursor.execute(insert_query, row)
        except sqlite3.Error as e:
            print("Error inserting data into database:", e)

    def process_csv(self, cursor):
        try:
            with open(self.source_file, 'r') as data:
                csv_reader = csv.reader(data, delimiter=',')
                next(csv_reader)  # Skip header row
                for row in csv_reader:
                    self.insert_data(cursor, row)
        except FileNotFoundError:
            print("Source file not found.")
            sys.exit(1)
        except PermissionError:
            print("Permission denied to access the source file.")
            sys.exit(1)
        except KeyboardInterrupt:
            print("Process interrupted by the user.")
            sys.exit(1)
        except Exception as e:
            print("Error processing CSV file:", e)
            sys.exit(1)

    def close_connection(self, connection):
        try:
            connection.commit()
            connection.close()
        except sqlite3.Error as e:
            print("Error closing database connection:", e)

def main():
    if len(sys.argv) != 2:
        print('Usage: python script_name.py source_file')
        sys.exit(1)

    source_file = Path(sys.argv[1])
    manager = DatabaseManager(source_file)
    connection, cursor = manager.create_database()
    manager.process_csv(cursor)
    manager.close_connection(connection)

if __name__ == "__main__":
    main()
