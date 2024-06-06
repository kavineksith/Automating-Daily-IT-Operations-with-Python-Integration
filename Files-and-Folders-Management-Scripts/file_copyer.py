import os
import sys
import shutil
from pathlib import Path

class FileCopyer:
    def __init__(self, source_path, destination_path):
        self.source_path = source_path
        self.destination_path = destination_path

    def copy_files(self):
        try:
            if not os.path.exists(self.source_path):
                raise FileNotFoundError(f'Source path "{self.source_path}" not found.')
            
            if not os.path.exists(self.destination_path):
                raise FileNotFoundError(f'Destination path "{self.destination_path}" not found.')
            
            shutil.copy2(self.source_path, self.destination_path)
            print('File copied successfully.')
        
        except shutil.SameFileError:
            print('Source and destination represent the same file.')
        except PermissionError:
            print('Permission denied.')
        except FileNotFoundError as e:
            print(e)
        except KeyboardInterrupt:
            print("Process interrupted by the user.")
            sys.exit(1)
        except Exception as e:
            print(f"An error occurred: {e}")

def main():
    source_path = Path(input('Source: '))
    destination_path = Path(input('Destination: '))

    copier = FileCopyer(source_path, destination_path)
    copier.copy_files()

if __name__ == "__main__":
    main()
    sys.exit(0)
