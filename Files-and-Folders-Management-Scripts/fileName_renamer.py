import os
import sys

class FileNameRenamer:
    def __init__(self, current_filename, new_filename):
        self.current_filename = current_filename
        self.new_filename = new_filename

    def rename_file(self):
        try:
            if not os.path.exists(self.current_filename):
                raise FileNotFoundError(f'File "{self.current_filename}" not found.')
            
            name, ext = os.path.splitext(self.current_filename)
            new_filename_with_ext = self.new_filename + ext
            
            os.rename(self.current_filename, new_filename_with_ext)
            print(f'File "{self.current_filename}" renamed to "{new_filename_with_ext}" successfully.')
        
        except PermissionError:
            print(f'Permission denied to rename "{self.current_filename}".')
        except FileNotFoundError as e:
            print(e)
        except KeyboardInterrupt:
            print("Process interrupted by the user.")
            sys.exit(1)
        except Exception as e:
            print(f"An error occurred: {e}")

def main():
    if len(sys.argv) != 3:
        print('Usage: fileName_renamer.py <current_fileName> <new_fileName>')
        sys.exit(1)

    current_filename = sys.argv[1]
    new_filename = sys.argv[2]

    renamer = FileNameRenamer(current_filename, new_filename)
    renamer.rename_file()

if __name__ == "__main__":
    main()
    sys.exit(0)
