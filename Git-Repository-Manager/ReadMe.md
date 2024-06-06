## Documentation : Local Git Repository Manager 

### Overview
This Python script serves as a command-line tool for managing Git repositories. It provides various functionalities such as initializing a repository, adding files, committing changes, pushing to and pulling from remote repositories, creating and switching branches, merging branches, and listing branches.

### Requirements
- Python 3.x
- Git installed and configured on the system

### Usage
1. Ensure that Git is installed and configured on your system.
2. Run the script and follow the menu prompts to perform Git repository management operations.
3. Provide input as requested for each operation.

### Implementation Details
#### Dependencies
- `os`, `sys`, `subprocess`: Standard Python libraries for system operations and subprocess execution.
- `shutil`: Used for file operations like copying directories.
- `pathlib.Path`: Provides object-oriented filesystem paths.

#### Custom Exception: `GitError`
- Custom exception class for Git-related errors.
- Inherits from `Exception`.
- Provides additional information about Git operation failures.

#### Class: `GitRepoManager`
- Methods:
  - `__init__(self, repo_path)`: Initializes the GitRepoManager object with the path to the Git repository.
  - Various methods for performing Git operations such as initializing repository, adding files, committing changes, pushing to and pulling from remote, creating and merging branches, listing branches, etc.

#### Function: `get_current_file_path()`
- Retrieves the directory path of the current script file.
- Utilizes `os.path` and `pathlib.Path` for path manipulation.
- Raises `OSError` if the path of the current script file cannot be determined.

#### Function: `main()`
- Provides a user-friendly interface for interacting with the Git repository manager.
- Presents a menu with options for various Git operations.
- Handles user input and calls corresponding methods of `GitRepoManager`.
- Gracefully handles exceptions and interrupts.

### Conclusion
This script provides a convenient way to manage Git repositories through a command-line interface. It simplifies common Git operations such as adding files, committing changes, and pushing to remote repositories, making Git workflow more efficient. With its intuitive menu system, users can easily perform repository management tasks without needing to memorize Git commands.

Kindly note that this project is developed solely for educational purposes, not intended for industrial use, as its sole intention lies within the realm of education. We emphatically underscore that this endeavor is not sanctioned for industrial application. It is imperative to bear in mind that any utilization of this project for commercial endeavors falls outside the intended scope and responsibility of its creators. Thus, we explicitly disclaim any liability or accountability for such usage.