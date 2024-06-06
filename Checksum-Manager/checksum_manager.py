import hashlib
import sys
from pathlib import Path


class ChecksumManager:
    def __init__(self, file_path, method=None, checksum=None):
        self.file_path = file_path
        self.method = method.lower() if method else None
        self.checksum = checksum

    def generate_checksum(self):
        try:
            with open(self.file_path, 'rb') as file:
                bytes_content = file.read()

                hash_function = getattr(hashlib, self.method, None)  # type: ignore
                if hash_function:
                    cypher = hash_function(bytes_content).hexdigest()
                    return cypher
                else:
                    raise ValueError(f"Invalid hash method: {self.method}")
        except FileNotFoundError:
            print(f"File '{self.file_path}' not found.")
            sys.exit(1)
        except PermissionError:
            print(f"Permission denied while accessing '{self.file_path}'.")
            sys.exit(1)
        except KeyboardInterrupt:
            print("Process interrupted by the user.")
            sys.exit(1)
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            sys.exit(1)

    def verify_checksum(self):
        if self.method is not None and self.checksum is not None:  # Check both method and checksum are provided
            computed_checksum = self.generate_checksum()
            if computed_checksum:
                if self.checksum == computed_checksum:
                    print("Checksum matched")
                else:
                    print("Checksum unmatched")
            else:
                print("Can't check the checksum")
        else:
            print("Checksum method and value are required for verification.")


def get_file_location():
    while True:
        location = Path(input('File Path: '))
        if location:
            return location
        else:
            print('File Path required...!!')


def get_checksum_method():
    while True:
        method = input('Checksum Method (sha1, sha224, sha256, sha384, sha512, md5): ')
        if method.lower() in hashlib.algorithms_guaranteed:
            return method
        else:
            print('Checksum method required...!!')


def get_checksum_value():
    while True:
        checksum = input('Checksum: ')
        if checksum:
            return checksum
        else:
            print('Checksum required...!!')


def main():

    if len(sys.argv) != 2:
        print("Usage: python checksum_manager.py purpose(generate or validate)")
        sys.exit(1)

    [purpose] = sys.argv[1:]

    if purpose.lower().strip() == "generate":
        file_location = get_file_location()
        checksum_method = get_checksum_method()

        if file_location and checksum_method:  # Check if file path and method are provided
            checksum_wizard = ChecksumManager(file_location, checksum_method)
            calculated_checksum = checksum_wizard.generate_checksum()
            print(f"Checksum: {calculated_checksum}")
        else:
            print("File location and checksum method are required for generating process.")
    elif purpose.lower().strip() == "validate":
        file_location = get_file_location()
        checksum_method = get_checksum_method()
        checksum_value = get_checksum_value()

        if file_location and checksum_method and checksum_value:  # Check if file path, method and value are provided
            manager_with_checksum = ChecksumManager(file_location, checksum_method, checksum_value)
            manager_with_checksum.verify_checksum()
        else:
            print("File location, checksum method and value are required for verification process.")
    else:
        print("Kindly specify your intended purpose method as either 'generate' to produce a checksum for the file, "
              "or 'validate' to authenticate the file against an existing checksum. This delineation ensures accurate "
              "execution of the checksum process, aligning with your distinct needs.")
        sys.exit(1)


if __name__ == "__main__":
    main()
    sys.exit(0)
