import sqlite3
import sys
import re

class TodoListManager:
    def __init__(self, db_file="todo.db"):
        self.db_file = db_file

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_file)
        self.conn.execute("PRAGMA foreign_keys = 1")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.conn:
            self.conn.close()

    def create_table(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS todos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task TEXT NOT NULL,
                    completed INTEGER DEFAULT 0
                )
            """)
            print("Table created successfully.")

    def add_task(self, task):
        with self.conn:
            self.conn.execute("INSERT INTO todos (task) VALUES (?)", (task,))
            print("Task added successfully.")

    def update_task(self, task_id, new_task):
        with self.conn:
            self.conn.execute("UPDATE todos SET task = ? WHERE id = ?", (new_task, task_id))
            print("Task updated successfully.")

    def delete_task(self, task_id):
        with self.conn:
            self.conn.execute("DELETE FROM todos WHERE id = ?", (task_id,))
            print("Task deleted successfully.")

    def mark_completed(self, task_id):
        with self.conn:
            self.conn.execute("UPDATE todos SET completed = 1 WHERE id = ?", (task_id,))
            print("Task marked as completed successfully.")

    def search_tasks(self, keyword):
        with self.conn:
            cursor = self.conn.execute("SELECT * FROM todos WHERE task LIKE ?", ('%' + keyword + '%',))
            tasks = cursor.fetchall()
            if tasks:
                print("\nMatching Tasks:")
                for task in tasks:
                    print(f"{task[0]}. {task[1]} {'(Completed)' if task[2] else ''}")
            else:
                print("No matching tasks found.")

    def view_all_tasks(self):
        with self.conn:
            cursor = self.conn.execute("SELECT * FROM todos")
            tasks = cursor.fetchall()
            if tasks:
                print("\nAll Tasks:")
                for task in tasks:
                    print(f"{task[0]}. {task[1]} {'(Completed)' if task[2] else ''}")
            else:
                print("\nNo tasks found.")

    def run(self):
        with self:
            self.create_table()
            try:
                while True:
                    print("\nTodo List Manager")
                    print("1. View All Tasks")
                    print("2. Add Task")
                    print("3. Update Task")
                    print("4. Delete Task")
                    print("5. Mark Task as Completed")
                    print("6. Search Tasks")
                    print("7. Exit")
                    choice = input("\nEnter your choice: ")
                    if choice == "1":
                        self.view_all_tasks()
                    elif choice == "2":
                        task = input("Enter the task: ").strip()
                        self.add_task(task)
                    elif choice == "3":
                        task_id = int(input("Enter the task ID to update: "))
                        new_task = input("Enter the updated task: ").strip()
                        self.update_task(task_id, new_task)
                    elif choice == "4":
                        task_id = int(input("Enter the task ID to delete: "))
                        self.delete_task(task_id)
                    elif choice == "5":
                        task_id = int(input("Enter the task ID to mark as completed: "))
                        self.mark_completed(task_id)
                    elif choice == "6":
                        keyword = input("Enter a keyword to search for in tasks: ").strip()
                        self.search_tasks(keyword)
                    elif choice == "7":
                        print("Exiting...")
                        break
                    else:
                        print("Invalid choice. Please enter a valid option.")
            except ValueError:
                print("Invalid input. Please enter a number from 1 to 7.")
            except KeyboardInterrupt:
                print("\n\nKeyboard interrupted. Exiting...")
                sys.exit(1)
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    db_file = "./todo_app.db"
    with TodoListManager(db_file) as manager:
        manager.run()
    sys.exit(0)

