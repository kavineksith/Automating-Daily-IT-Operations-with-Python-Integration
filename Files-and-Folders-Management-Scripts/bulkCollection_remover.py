import sys
import shutil
from pathlib import Path

class ItemRemover:
    def __init__(self, location):
        self.location = location

    def remove_items(self):
        try:
            if not self.location.exists():
                raise FileNotFoundError(f"Path '{self.location}' does not exist.")
            
            for item in self.location.iterdir():
                try:
                    if item.is_file():
                        item.unlink()
                    elif item.is_dir():
                        shutil.rmtree(item)
                except PermissionError as e:
                    print(f"Permission error occurred while removing '{item}': {e}")
                except Exception as e:
                    print(f"An error occurred while removing '{item}': {e}")

            print("Items removed successfully.")
        except FileNotFoundError as fnfe:
            print(f"File not found error: {fnfe}")
        except KeyboardInterrupt:
            print("Process interrupted by the user.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

def get_location():
    while True:
        location = Path(input("Location: "))
        if location:
            return location
        else:
            print('Please provide a valid location.')

def main():
    location = get_location()
    remover = ItemRemover(location)
    remover.remove_items()

if __name__ == "__main__":
    main()
    sys.exit(0)
