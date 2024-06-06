import os
import sys

class ExtensionRenamer:
    def __init__(self, file_name, new_extension):
        self.file_name = file_name
        self.new_extension = new_extension

    def rename_extension(self):
        try:
            if not os.path.exists(self.file_name):
                raise FileNotFoundError(f'File "{self.file_name}" not found.')
            
            name, ext = os.path.splitext(self.file_name)
            new_file_name = f"{name}{self.new_extension}"
            os.rename(self.file_name, new_file_name)
            print(f'Extension renamed successfully: {self.file_name} -> {new_file_name}')
        
        except PermissionError:
            print(f'Permission denied to rename "{self.file_name}".')
        except FileNotFoundError as e:
            print(e)
        except KeyboardInterrupt:
            print("Process interrupted by the user.")
            sys.exit(1)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            sys.exit(1)

def main():
    if len(sys.argv) != 3:
        print('Usage: python extension_renamer.py <file_name> <new_extension>')
        sys.exit(1)

    file_name = sys.argv[1]
    new_extension = sys.argv[2]

    renamer = ExtensionRenamer(file_name, new_extension)
    renamer.rename_extension()

if __name__ == "__main__":
    main()
    sys.exit(0)
