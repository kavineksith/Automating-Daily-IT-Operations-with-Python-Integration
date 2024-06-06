import os
import sys
from pathlib import Path

class FolderRemover:
    def __init__(self, location):
        self.location = location

    def remove_folder(self):
        try:
            if not os.path.exists(self.location):
                raise FileNotFoundError(f'Folder "{self.location}" not found.')
            
            if os.path.isdir(self.location):
                os.rmdir(self.location)
                print(f'Folder "{self.location}" removed successfully.')
            else:
                raise NotADirectoryError(f'"{self.location}" is not a folder or it is not empty.')

        except PermissionError:
            print(f'Permission denied to remove folder "{self.location}".')
        except FileNotFoundError as e:
            print(e)
        except NotADirectoryError as e:
            print(e)
        except KeyboardInterrupt:
            print("Process interrupted by the user.")
            sys.exit(1)
        except Exception as e:
            print(f"An error occurred: {e}")

def main():
    location = Path(input("Location : ")) # getting the path of directory
    remover = FolderRemover(location)
    remover.remove_folder()

if __name__ == "__main__":
    main()
    sys.exit(0)
