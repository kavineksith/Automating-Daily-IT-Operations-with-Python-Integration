import os
import sys

class DomainReplacer:
    def __init__(self, source_file, export_file, old_domain, new_domain):
        self.source_file = source_file
        self.export_file = export_file
        self.old_domain = old_domain
        self.new_domain = new_domain

    def domain_replacer(self, email):
        if "@" + self.old_domain in email:
            index = email.index("@" + self.old_domain)
            new_email = email[:index] + "@" + self.new_domain
            return new_email
        return email

    def data_processing(self):
        old_emails = []
        try:
            if not os.path.exists(self.source_file):
                raise FileNotFoundError("Source file doesn't exist.")
            
            with open(self.source_file, 'r') as legacy_list:
                for row in legacy_list:
                    old_emails.append(row.strip())
        except PermissionError:
            print("Permission denied to access source file.")
            sys.exit(1)
        except FileNotFoundError as e:
            print(e)
            sys.exit(1)
        
        return old_emails

    def data_transformation(self):
        new_emails = []
        try:
            if os.path.exists(self.export_file):
                raise FileExistsError("Output file already exists. Please choose a different file name.")
            
            for email in self.data_processing():
                new_emails.append(self.domain_replacer(email))
            
            with open(self.export_file, 'w') as modern_list:
                for email in new_emails:
                    modern_list.write(email + '\n')
        except PermissionError:
            print("Permission denied to write to the output file.")
            sys.exit(1)
        except FileExistsError as e:
            print(e)
            sys.exit(1)
        except KeyboardInterrupt:
            print("Process interrupted by the user.")
            sys.exit(1)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            sys.exit(1)

def main():
    if len(sys.argv) != 5:
        print('Usage: python script_name.py input_file output_file old_domain new_domain')
        sys.exit(1)
    
    source_file, export_file, old_domain, new_domain = sys.argv[1:]
    replacer = DomainReplacer(source_file, export_file, old_domain, new_domain)
    replacer.data_transformation()

if __name__ == "__main__":
    main()
