import os
import sys
import subprocess
import shutil
from pathlib import Path

class GitError(Exception):
    """Custom exception class for Git-related errors."""
    def __init__(self, message="Git operation failed", original_exception=None):
        super().__init__(message)
        self.original_exception = original_exception
    
    def __str__(self):
        if self.original_exception:
            return f"{self.__class__.__name__}: {self.args[0]}. Original exception: {self.original_exception.__class__.__name__}: {str(self.original_exception)}"
        else:
            return f"{self.__class__.__name__}: {self.args[0]}"

def get_current_file_path():
    """
    Retrieve the directory path of the current script file.

    Returns:
        Path: The directory path of the current script file.
        
    Raises:
        OSError: If the path of the current script file cannot be determined.
    """
    try:
        current_file = os.path.abspath(__file__)
        return Path(current_file).parent
    except OSError as e:
        raise OSError("Failed to determine the path of the current script file.") from e

class GitRepoManager:
    def __init__(self, repo_path):
        self.repo_path = repo_path

    def init_repo(self):
        try:
            if os.path.exists(self.repo_path):
                raise GitError("Repository already exists.")
            # Replace <source_repo_path> with the path to an existing Git repository
            # source_repo_path = "<source_repo_path>"
            source_repo_path = get_current_file_path() / "existing_repository"
            shutil.copytree(source_repo_path, self.repo_path)
            subprocess.run(["git", "init", self.repo_path], check=True)
            print("Initialized Git repository.")
        except (subprocess.CalledProcessError, OSError, GitError, shutil.Error) as e:
            print(f"Error: {e}")

    def add_files(self, file_paths):
        try:
            if not os.path.exists(self.repo_path):
                raise GitError("Repository does not exist.")
            subprocess.run(["git", "add"] + file_paths, cwd=self.repo_path, check=True)
            print("Files added to staging area.")
        except (subprocess.CalledProcessError, OSError, GitError) as e:
            print(f"Error: {e}")

    def commit_changes(self, message):
        try:
            if not os.path.exists(self.repo_path):
                raise GitError("Repository does not exist.")
            subprocess.run(["git", "commit", "-m", message], cwd=self.repo_path, check=True)
            print("Changes committed.")
        except (subprocess.CalledProcessError, OSError, GitError) as e:
            print(f"Error: {e}")

    def push_to_remote(self, remote_url, branch="main"):
        try:
            if not os.path.exists(self.repo_path):
                raise GitError("Repository does not exist.")
            subprocess.run(["git", "remote", "add", "origin", remote_url], cwd=self.repo_path, check=True)
            subprocess.run(["git", "push", "-u", "origin", branch], cwd=self.repo_path, check=True)
            print("Changes pushed to remote repository.")
        except (subprocess.CalledProcessError, OSError, GitError) as e:
            print(f"Error: {e}")

    def create_branch(self, branch_name):
        try:
            if not os.path.exists(self.repo_path):
                raise GitError("Repository does not exist.")
            subprocess.run(["git", "checkout", "-b", branch_name], cwd=self.repo_path, check=True)
            print(f"New branch '{branch_name}' created and switched to.")
        except (subprocess.CalledProcessError, OSError, GitError) as e:
            print(f"Error: {e}")

    def merge_branch(self, branch_name):
        try:
            if not os.path.exists(self.repo_path):
                raise GitError("Repository does not exist.")
            subprocess.run(["git", "merge", branch_name], cwd=self.repo_path, check=True)
            print(f"Merged changes from branch '{branch_name}'.")
        except (subprocess.CalledProcessError, OSError, GitError) as e:
            print(f"Error: {e}")

    def pull_from_remote(self, remote_url, branch="main"):
        try:
            if not os.path.exists(self.repo_path):
                raise GitError("Repository does not exist.")
            subprocess.run(["git", "pull", "origin", branch], cwd=self.repo_path, check=True)
            print("Pulled changes from remote repository.")
        except (subprocess.CalledProcessError, OSError, GitError) as e:
            print(f"Error: {e}")

    def checkout_branch(self, branch_name):
        try:
            if not os.path.exists(self.repo_path):
                raise GitError("Repository does not exist.")
            subprocess.run(["git", "checkout", branch_name], cwd=self.repo_path, check=True)
            print(f"Switched to branch '{branch_name}'.")
        except (subprocess.CalledProcessError, OSError, GitError) as e:
            print(f"Error: {e}")

    def list_branches(self):
        try:
            if not os.path.exists(self.repo_path):
                raise GitError("Repository does not exist.")
            result = subprocess.run(["git", "branch"], cwd=self.repo_path, capture_output=True, text=True, check=True)
            branches = [branch.strip() for branch in result.stdout.split("\n")]
            print("Branches:")
            for branch in branches:
                print(branch)
        except (subprocess.CalledProcessError, OSError, GitError) as e:
            print(f"Error: {e}")

def main():
    print("Welcome to Git Repository Manager!")

    repo_path = input("Enter path for the repository: ")
    manager = GitRepoManager(repo_path)

    while True:
        try:
            print("\nMenu:")
            print("1. Initialize Repository")
            print("2. Add Files")
            print("3. Commit Changes")
            print("4. Push to Remote Repository")
            print("5. Create Branch")
            print("6. Merge Branch")
            print("7. Pull from Remote Repository")
            print("8. Checkout Branch")
            print("9. List Branches")
            print("10. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                manager.init_repo()
            elif choice == '2':
                file_paths = input("Enter file paths (comma-separated): ").split(",")
                manager.add_files(file_paths)
            elif choice == '3':
                message = input("Enter commit message: ")
                manager.commit_changes(message)
            elif choice == '4':
                remote_url = input("Enter remote repository URL: ")
                branch = input("Enter branch name (default: main): ") or "main"
                manager.push_to_remote(remote_url, branch)
            elif choice == '5':
                branch_name = input("Enter branch name: ")
                manager.create_branch(branch_name)
            elif choice == '6':
                branch_name = input("Enter branch name to merge: ")
                manager.merge_branch(branch_name)
            elif choice == '7':
                remote_url = input("Enter remote repository URL: ")
                branch = input("Enter branch name (default: main): ") or "main"
                manager.pull_from_remote(remote_url, branch)
            elif choice == '8':
                branch_name = input("Enter branch name to switch: ")
                manager.checkout_branch(branch_name)
            elif choice == '9':
                manager.list_branches()
            elif choice == '10':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 10.")
        except KeyboardInterrupt:
            print("Process interrupted by the user.")
            sys.exit(1)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
    sys.exit(0)

