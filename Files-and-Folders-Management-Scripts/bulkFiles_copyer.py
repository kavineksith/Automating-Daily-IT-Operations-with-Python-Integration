import sys
import shutil
from pathlib import Path

class FileCopier:
    def __init__(self, source_path, destination_path):
        self.source_path = source_path
        self.destination_path = destination_path
        self.copied_files_count = 0
        self.uncopied_files_count = 0
        self.folders_count = 0

    def copy_files(self):
        try:
            if not self.source_path.exists():
                raise FileNotFoundError(f"Source path '{self.source_path}' does not exist.")
            if not self.destination_path.exists():
                raise FileNotFoundError(f"Destination path '{self.destination_path}' does not exist.")

            for file in self.source_path.iterdir():
                if file.is_file():
                    try:
                        shutil.copy2(file, self.destination_path)
                        self.copied_files_count += 1
                    except shutil.SameFileError:
                        print(f"{file} :- Source and destination represent the same file.")
                        self.uncopied_files_count += 1
                    except PermissionError:
                        print(f"{file} :- Permission denied.")
                        self.uncopied_files_count += 1
                    except Exception as e:
                        print(f"{file} :- Error occurred while copying file: {e}")
                        self.uncopied_files_count += 1
                elif file.is_dir():
                    self.folders_count += 1

            # Statistics report about operation
            print(f"\nTotal Files Count: {self.copied_files_count + self.uncopied_files_count}")
            print(f"Total Copied Files Count: {self.copied_files_count} / Total Uncopied Files Count: {self.uncopied_files_count}")
            print(f"Total Folders Count: {self.folders_count}\n")

        except FileNotFoundError as e:
            print(e)
        except KeyboardInterrupt:
            print("Process interrupted by the user.")
            sys.exit(1)
        except Exception as e:
            print(f"An error occurred: {e}")

def get_paths():
    while True:
        source_path = Path(input("Source: "))
        destination_path = Path(input("Destination: "))
        if source_path and destination_path:
            return source_path, destination_path
        else:
            print("Please provide valid paths.")

def main():
    source_path, destination_path = get_paths()
    copier = FileCopier(source_path, destination_path)
    copier.copy_files()

if __name__ == "__main__":
    main()
    sys.exit(0)
