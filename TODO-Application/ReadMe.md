## Documentation : Todo List Manager 

### Overview
The Todo List Manager script provides a command-line interface for managing a todo list stored in an SQLite database. It allows users to add, update, delete, mark tasks as completed, search tasks by keyword, and view all tasks.

### Requirements
- Python 3.x
- SQLite database

### Usage
1. Ensure Python and SQLite are installed on your system.
2. Run the script and follow the menu prompts to perform todo list management operations.
3. Provide input as requested for each operation.

### Implementation Details
#### Dependencies
- `sqlite3`: Python standard library for SQLite database operations.
- `sys`: Python standard library for system-specific parameters and functions.
- `re`: Python regular expression operations for string matching.

#### Class: `TodoListManager`
- Methods:
  - `__init__(self, db_file)`: Initializes the TodoListManager object with the path to the SQLite database file.
  - `__enter__(self)`: Opens a connection to the SQLite database.
  - `__exit__(self, exc_type, exc_value, traceback)`: Closes the connection to the SQLite database.
  - `create_table(self)`: Creates the `todos` table if it does not exist in the database.
  - `add_task(self, task)`: Adds a new task to the database.
  - `update_task(self, task_id, new_task)`: Updates an existing task in the database.
  - `delete_task(self, task_id)`: Deletes a task from the database.
  - `mark_completed(self, task_id)`: Marks a task as completed in the database.
  - `search_tasks(self, keyword)`: Searches tasks in the database based on a keyword.
  - `view_all_tasks(self)`: Displays all tasks stored in the database.
  - `run(self)`: Runs the todo list management application, displaying a menu for users to interact with.

#### Function: `get_current_file_path()`
- Retrieves the directory path of the current script file.
- Utilizes `os.path` and `pathlib.Path` for path manipulation.
- Raises `OSError` if the path of the current script file cannot be determined.

#### Function: `main()`
- Provides a user-friendly interface for interacting with the Todo List Manager.
- Presents a menu with options for various todo list management operations.
- Handles user input and calls corresponding methods of `TodoListManager`.
- Gracefully handles exceptions and interrupts.

### Conclusion
This script simplifies todo list management through a command-line interface, providing essential functionalities such as adding, updating, deleting, and searching tasks. By leveraging SQLite as the backend database, it offers a lightweight and portable solution for organizing tasks. With its intuitive menu system, users can easily interact with their todo lists without needing a separate application.

## **License**
This project is licensed under the MIT License. See the [LICENSE](https://github.com/kavineksith/Automating-Daily-IT-Operations-with-Python-Integration/blob/main/LICENSE) file for details.

### **Disclaimer:**
Kindly note that this project is developed solely for educational purposes, not intended for industrial use, as its sole intention lies within the realm of education. We emphatically underscore that this endeavor is not sanctioned for industrial application. It is imperative to bear in mind that any utilization of this project for commercial endeavors falls outside the intended scope and responsibility of its creators. Thus, we explicitly disclaim any liability or accountability for such usage.