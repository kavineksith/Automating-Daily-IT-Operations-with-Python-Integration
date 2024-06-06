from pathlib import Path
import os
import sys

class DataUploader:
    def __init__(self, source_file, export_file):
        self.source_file = source_file
        self.export_file = export_file

    def upload_data(self):
        try:
            if not os.path.exists(self.source_file):
                print('Source file not found.')
                sys.exit(1)
            if os.path.exists(self.export_file):
                print('Export file already exists.')
                sys.exit(1)

            with open(self.source_file, 'r') as data:
                with open(self.export_file, 'a') as new_data:
                    for row in data:
                        new_string = ' '.join(row.split())
                        clean_string = new_string.replace(" ", ",")
                        new_data.writelines(clean_string + '\n')
        except FileNotFoundError:
            print("Source file not found.")
            sys.exit(1)
        except PermissionError:
            print("Permission denied to access the source or export file.")
            sys.exit(1)
        except KeyboardInterrupt:
            print("Process interrupted by the user.")
            sys.exit(1)
        except Exception as e:
            print("Error uploading data:", e)
            sys.exit(1)

def main():
    if len(sys.argv) != 3:
        print('Usage: python script_name.py source_file export_file')
        sys.exit(1)

    source_file = Path(sys.argv[1])
    export_file = Path(sys.argv[2])

    uploader = DataUploader(source_file, export_file)
    uploader.upload_data()

if __name__ == "__main__":
    main()
