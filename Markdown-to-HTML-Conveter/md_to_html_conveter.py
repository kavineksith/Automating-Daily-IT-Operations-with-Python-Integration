import sys
import markdown
from pathlib import Path

class MarkdownToHTMLConverter:
    def __init__(self, markdown_file_path):
        self.markdown_file_path = Path(markdown_file_path)
        self.html_content = ""
    
    def convert_to_html(self):
        try:
            with self.markdown_file_path.open('r') as markdown_file:
                markdown_text = markdown_file.read()
                self.html_content = markdown.markdown(markdown_text)
        except FileNotFoundError:
            print("Error: File not found.")
            sys.exit(1)
        except FileExistsError:
            print("Error: Output file already exists.")
            sys.exit(1)
        except KeyboardInterrupt:
            print("\nConversion interrupted by user.")
            sys.exit(1)
        except ValueError:
            print("Error: Invalid input format.")
            sys.exit(1)
        except Exception as e:
            print("An unexpected error occurred:", str(e))
            sys.exit(1)
    
    def save_html_to_file(self, output_file_path):
        try:
            output_file_path = Path(output_file_path)
            with output_file_path.open('w') as html_file:
                html_file.write(self.html_content)
        except FileNotFoundError:
            print("Error: Output directory not found.")
            sys.exit(1)
        except FileExistsError:
            print("Error: Output file already exists.")
            sys.exit(1)
        except Exception as e:
            print("An unexpected error occurred:", str(e))
            sys.exit(1)

if __name__ == "__main__":
    try:
        input_file_path = input("Enter the path to the Markdown file: ")
        output_file_path = input("Enter the path to save the HTML file: ")
        
        converter = MarkdownToHTMLConverter(input_file_path)
        converter.convert_to_html()
        converter.save_html_to_file(output_file_path)
        
        print("Markdown to HTML conversion successful!")
    except KeyboardInterrupt:
        print("\nOperation interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print("An unexpected error occurred:", str(e))
        sys.exit(1)
