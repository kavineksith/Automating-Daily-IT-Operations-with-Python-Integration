import os
import sys
from pathlib import Path
from PIL import Image # type: ignore

class ImageProcessor:
    def __init__(self, gallery, input_format, output_format, width, height, rotate):
        self.gallery_path = gallery
        self.input_format = input_format.lower()
        self.output_format = output_format.lower()
        self.width = width
        self.height = height
        self.rotate = rotate
        
    def process_images(self):
        try:
            # Check if gallery directory exists
            if not os.path.exists(self.gallery_path):
                raise FileNotFoundError(f"Directory '{self.gallery_path}' not found.")
            
            for img_name in os.listdir(self.gallery_path):
                if not img_name.startswith('.') and self.input_format in img_name.lower():
                    img_path = os.path.join(self.gallery_path, img_name)
                    new_name = os.path.splitext(img_path)[0]
                    new_path = f'{new_name}.{self.output_format}'

                    # Check if output file already exists
                    if os.path.exists(new_path):
                        raise FileExistsError(f"Output file '{new_path}' already exists.")

                    image = Image.open(img_path)
                    resized_image = image.convert('RGB').resize((self.width, self.height)).rotate(self.rotate)
                    resized_image.save(new_path, self.output_format.upper())

            print("Image processing completed successfully!")
        except PermissionError as pe:
            print(f"Permission error: {pe}")
        except FileExistsError as fee:
            print(f"File exists error: {fee}")
        except FileNotFoundError as fnfe:
            print(f"File not found error: {fnfe}")
        except ValueError:
            print("Error: Width and height must be integer values.")
        except KeyboardInterrupt:
            print("Process interrupted by the user.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

def main():
    try:
        # Prompt for user input
        gallery = Path(input("Enter the gallery location: "))
        input_format = input("Enter the input image format (e.g., 'tiff', 'jpeg'): ")
        output_format = input("Enter the output image format (e.g., 'jpeg'): ")
        width = int(input("Enter the width for resizing (in pixels): "))
        height = int(input("Enter the height for resizing (in pixels): "))
        rotate = int(input("Enter the rotation degrees (e.g., 90, 180, -90): "))

        # Create ImageProcessor instance and process images
        processor = ImageProcessor(gallery, input_format, output_format, width, height, rotate)
        processor.process_images()
    except ValueError:
        print("Error: Width and height must be integer values.")
    except KeyboardInterrupt:
        print("Process interrupted by the user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
    sys.exit(0)
