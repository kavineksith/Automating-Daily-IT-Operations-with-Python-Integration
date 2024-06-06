import sys
import shutil
from pathlib import Path

class FileMover:
    def __init__(self, source_path, destination_path):
        self.source_path = source_path
        self.destination_path = destination_path
        self.moved_files_count = 0
        self.unmoved_files_count = 0
        self.folders_count = 0

    def move_files(self):
        try:
            if not self.source_path.exists():
                raise FileNotFoundError(f"Source path '{self.source_path}' does not exist.")
            if not self.destination_path.exists():
                raise FileNotFoundError(f"Destination path '{self.destination_path}' does not exist.")

            for file in self.source_path.iterdir():
                if file.is_file():
                    try:
                        shutil.move(file, self.destination_path)
                        self.moved_files_count += 1
                    except shutil.SameFileError:
                        print(f"{file} :- Source and destination represent the same file.")
                        self.unmoved_files_count += 1
                    except PermissionError:
                        print(f"{file} :- Permission denied.")
                        self.unmoved_files_count += 1
                    except Exception as e:
                        print(f"{file} :- Error occurred while moving file: {e}")
                        self.unmoved_files_count += 1
                elif file.is_dir():
                    self.folders_count += 1

            # Statistics report about operation
            print(f"\nTotal Files Count: {self.moved_files_count + self.unmoved_files_count}")
            print(f"Total Moved Files Count: {self.moved_files_count} / Total Unmoved Files Count: {self.unmoved_files_count}")
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
    mover = FileMover(source_path, destination_path)
    mover.move_files()

if __name__ == "__main__":
    main()
    sys.exit(0)
