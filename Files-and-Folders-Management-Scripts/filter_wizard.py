import os
import sys

class ContentFilter:
    def __init__(self, location):
        self.location = location

    def filter_content(self):
        try:
            if not os.path.exists(self.location):
                raise FileNotFoundError(f'Location "{self.location}" not found.')
            
            file_count = 0
            folder_count = 0
            
            for name in os.listdir(self.location):
                fullname = os.path.join(self.location, name)
                if os.path.isdir(fullname):
                    print(f"{fullname} is a directory")
                    folder_count += 1
                else:
                    print(f"{fullname} is a file")
                    file_count += 1

            print('\n---- Total Count ----')
            print(f'Files Count : {file_count}')
            print(f'Folder Count : {folder_count}\n')

        except PermissionError:
            print(f'Permission denied to access location "{self.location}".')
        except FileNotFoundError as e:
            print(e)
        except KeyboardInterrupt:
            print("Process interrupted by the user.")
            sys.exit(1)
        except Exception as e:
            print(f"An error occurred: {e}")

def main():
    location = os.getcwd()
    filter_instance = ContentFilter(location)
    filter_instance.filter_content()

if __name__ == "__main__":
    main()
    sys.exit(0)
