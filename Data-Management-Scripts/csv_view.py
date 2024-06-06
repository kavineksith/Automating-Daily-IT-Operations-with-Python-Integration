import os
import sys
import csv
from pathlib import Path

class CSVPreviewer:
    def __init__(self, source_file):
        self.source_file = source_file

    def preview_csv(self):
        try:
            if not os.path.exists(self.source_file):
                print('Source file not found.')
                sys.exit(1)

            with open(self.source_file, 'r') as data:
                csv_reader = csv.reader(data, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    print(' '.join(row))
                    line_count += 1
                print(f'\nProcessed {line_count} lines.')
        except FileNotFoundError:
            print("Source file not found.")
            sys.exit(1)
        except PermissionError:
            print("Permission denied to access the source file.")
            sys.exit(1)
        except KeyboardInterrupt:
            print("Process interrupted by the user.")
            sys.exit(1)
        except Exception as e:
            print("Error processing CSV file:", e)
            sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print('Usage: python script_name.py source_file')
        sys.exit(1)

    source_file = Path(sys.argv[1])
    previewer = CSVPreviewer(source_file)
    previewer.preview_csv()

if __name__ == "__main__":
    main()
