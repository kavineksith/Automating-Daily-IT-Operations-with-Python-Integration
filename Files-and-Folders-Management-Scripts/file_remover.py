import os
import sys
from pathlib import Path

class FileRemover:
    def __init__(self, file_location):
        self.file_location = file_location

    def remove_file(self):
        try:
            if not os.path.exists(self.file_location):
                raise FileNotFoundError(f'File "{self.file_location}" not found.')
            
            if os.path.isdir(self.file_location):
                raise ValueError('Provided location is a directory, not a file.')
            
            os.remove(self.file_location)
            print(f'File "{self.file_location}" removed successfully.')
        
        except PermissionError:
            print(f'Permission denied to remove "{self.file_location}".')
        except FileNotFoundError as e:
            print(e)
        except ValueError as e:
            print(e)
        except KeyboardInterrupt:
            print("Process interrupted by the user.")
            sys.exit(1)
        except Exception as e:
            print(f"An error occurred: {e}")

def main():
    file_location = Path(input("Location: "))
    remover = FileRemover(file_location)
    remover.remove_file()

if __name__ == "__main__":
    main()
    sys.exit(0)
