import os
import shutil
import logging

class File:
    def __init__(self, name, path):
        self.name = name
        self.path = path

    @property
    def extension(self):
        return os.path.splitext(self.name)[1]

class Directory:
    def __init__(self, path):
        self.path = path

    def create(self):
        if not os.path.exists(self.path):
            os.makedirs(self.path)

class FileManager:
    def __init__(self, source_path, destination_path):
        self.source_path = source_path
        self.destination_path = destination_path

    def create_destination_directories(self):
        try:
            directories = ['audios', 'videos', 'images', 'documents', 'formats', 'scripts', 'general']
            for directory in directories:
                full_path = os.path.join(self.destination_path, directory)
                Directory(full_path).create()
        except Exception as e:
            logging.error(f"Failed to create destination directories: {str(e)}")
            raise

    def file_identifier(self):
        try:
            os.chdir(self.source_path)
            for file_name in os.listdir():
                if os.path.isfile(file_name):
                    file = File(file_name, os.path.join(self.source_path, file_name))
                    self.file_transformer(file)
        except FileNotFoundError:
            logging.error("Source directory not found.")
            raise
        except PermissionError:
            logging.error("Permission denied while accessing source directory.")
            raise
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")
            raise

    def file_transformer(self, file):
        try:
            audios, videos, images, documents, formats, scripts = self.format_lake()

            if file.extension in audios:
                directory = 'audios'
            elif file.extension in videos:
                directory = 'videos'
            elif file.extension in images:
                directory = 'images'
            elif file.extension in documents:
                directory = 'documents'
            elif file.extension in formats:
                directory = 'formats'
            elif file.extension in scripts:
                directory = 'scripts'
            else:
                directory = 'general'

            dest_file_path = os.path.join(self.destination_path, directory, file.name)
            if os.path.exists(dest_file_path):
                if self.file_overwriting_wizard(file.name, directory):
                    shutil.move(file.path, os.path.join(self.destination_path, directory))
                    logging.info(f"{file.name} overwritten in {directory}")
                else:
                    logging.info(f"{file.name} not moved.")
            else:
                shutil.move(file.path, os.path.join(self.destination_path, directory))
                logging.info(f"{file.name} moved to {directory}")
        except Exception as e:
            logging.error(f"An error occurred during file transformation: {str(e)}")
            raise

    def file_overwriting_wizard(self, file_name, directory):
        while True:
            user_choice = input(f'{file_name} exists in {directory} folder. Do you want to overwrite this file? (Yes/No): ').lower()
            if user_choice in ['yes', 'no']:
                return user_choice == 'yes'
            else:
                print("Please enter 'Yes' or 'No' as your answer.")

    @staticmethod
    def format_lake():
        return ['.mp3', '.ogg', '.wav'], ['.webm', '.mov', '.mp4', '.mkv', '.avi'], \
               ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg'], \
               ['.txt', '.doc', '.docx', '.xlsx', '.pptx', '.pdf'], \
               ['.sql', '.json', '.xml'], \
               ['.ps', '.sh', '.py', '.js']

if __name__ == "__main__":
    import sys

    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

    if len(sys.argv) != 3:
        print('Usage: python file_manager.py source_path destination_path')
        sys.exit(1)

    source_path, destination_path = sys.argv[1:]
    file_manager = FileManager(source_path, destination_path)
    file_manager.create_destination_directories()
    file_manager.file_identifier()
