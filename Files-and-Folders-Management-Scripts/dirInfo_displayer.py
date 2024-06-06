import os
import sys
from pathlib import Path
from datetime import datetime

class DirectoryDetails:
    def __init__(self, local_path):
        self.local_path = local_path
        self.file_count = 0
        self.folder_count = 0

    def get_dir_size(self, start_path='.'):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(start_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                if not os.path.islink(fp):
                    total_size += os.path.getsize(fp)
        return total_size

    def print_details(self):
        try:
            if not Path(self.local_path).exists():
                raise FileNotFoundError(f'Directory "{self.local_path}" not found.')
            
            for item in os.listdir(self.local_path):
                item_path = os.path.join(self.local_path, item)
                if os.path.isdir(item_path):
                    self.print_folder_details(item, item_path)
                else:
                    self.print_file_details(item, item_path)
            
            print(f'Total Files Count: {self.file_count}')
            print(f'Total Folder Count: {self.folder_count}')
        
        except PermissionError:
            print(f'Permission denied for accessing "{self.local_path}".')
        except FileNotFoundError as e:
            print(e)

    def print_file_details(self, item, item_path):
        try:
            file_size = os.path.getsize(item_path)
            access_time = os.path.getatime(item_path)
            change_time = os.path.getctime(item_path)
            modified_time = os.path.getmtime(item_path)
            self.file_count += 1

            print(f'File Name: {item}\nFile Path: {item_path}\nFile Size: {(file_size / 1024):.2f} KB')
            print(f'Last Access Date-Time: {datetime.fromtimestamp(access_time).strftime("%Y-%m-%d %H:%M:%S")}')
            print(f'Last Change Date-Time: {datetime.fromtimestamp(change_time).strftime("%Y-%m-%d %H:%M:%S")}')
            print(f'Last Modification Date-Time: {datetime.fromtimestamp(modified_time).strftime("%Y-%m-%d %H:%M:%S")}\n')
        
        except PermissionError:
            print(f'Permission denied for accessing "{item_path}".')

    def print_folder_details(self, folder_name, folder_path):
        try:
            folder_size = self.get_dir_size(folder_path)
            access_time = os.path.getatime(folder_path)
            change_time = os.path.getctime(folder_path)
            modified_time = os.path.getmtime(folder_path)
            self.folder_count += 1

            print(f'Folder Name: {folder_name}\nFolder Path: {folder_path}\nFolder Size: {(folder_size / 1024 ** 2):.2f} MB')
            print(f'Last Access Date-Time: {datetime.fromtimestamp(access_time).strftime("%Y-%m-%d %H:%M:%S")}')
            print(f'Last Change Date-Time: {datetime.fromtimestamp(change_time).strftime("%Y-%m-%d %H:%M:%S")}')
            print(f'Last Modification Date-Time: {datetime.fromtimestamp(modified_time).strftime("%Y-%m-%d %H:%M:%S")}\n')

        except PermissionError:
            print(f'Permission denied for accessing "{folder_path}".')

def main():
    try:
        local_path = input('Location: ')
        details = DirectoryDetails(local_path)
        details.print_details()
    except KeyboardInterrupt:
        print("Process interrupted by the user.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
    sys.exit(0)
