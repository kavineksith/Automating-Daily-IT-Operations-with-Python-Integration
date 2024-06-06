import os
import sys

class ContentFilter:
    def __init__(self, location):
        self.location = location

    def scan_directory(self, directory):
        file_count = 0
        folder_count = 0

        for name in os.listdir(directory):
            fullname = os.path.join(directory, name)
            if os.path.isdir(fullname):
                print(f"{fullname} is a directory")
                folder_count += 1
                file_count_temp, folder_count_temp = self.scan_directory(fullname)
                file_count += file_count_temp
                folder_count += folder_count_temp
            else:
                print(f"{fullname} is a file")
                file_count += 1

        return file_count, folder_count

    def filter_content(self):
        try:
            if not os.path.exists(self.location):
                raise FileNotFoundError(f'Location "{self.location}" not found.')
            
            file_count, folder_count = self.scan_directory(self.location)

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
