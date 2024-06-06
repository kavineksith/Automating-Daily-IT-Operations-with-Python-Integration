import json
import sys

class ContactManager:
    def __init__(self, filename):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.filename, 'r') as file:
                contacts = json.load(file)
            return contacts
        except FileNotFoundError:
            print(f"Warning: Contacts file '{self.filename}' not found. Creating new file.")
            return []
        except json.JSONDecodeError:
            raise ValueError("Error: Unable to load contacts. Invalid JSON format.")

    def save_contacts(self):
        try:
            with open(self.filename, 'a') as file:
                json.dump(self.contacts, file, indent=4)
        except Exception as e:
            raise IOError(f"Error occurred while saving contacts: {e}")

    def add_contact(self, name, phone, email):
        contact = {'name': name, 'phone': phone, 'email': email}
        self.contacts.append(contact)
        self.save_contacts()

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            del self.contacts[index]
            self.save_contacts()
        else:
            raise ValueError("Error: Invalid contact index.")

    def display_contacts(self):
        if self.contacts:
            print("Contacts:")
            for i, contact in enumerate(self.contacts):
                print(f"{i+1}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
        else:
            print("No contacts available.")

def main():
    filename = "contacts.json"
    try:
        contact_manager = ContactManager(filename)

        while True:
            print("\nContact Manager")
            print("1. Add Contact")
            print("2. Delete Contact")
            print("3. Display Contacts")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                name = input("Enter name: ")
                phone = input("Enter phone number: ")
                email = input("Enter email address: ")
                contact_manager.add_contact(name, phone, email)
                print("Contact added successfully.")
            elif choice == '2':
                try:
                    index = int(input("Enter index of contact to delete: ")) - 1
                    contact_manager.delete_contact(index)
                    print("Contact deleted successfully.")
                except ValueError:
                    print("Error: Invalid index. Please enter a valid integer.")
            elif choice == '3':
                contact_manager.display_contacts()
            elif choice == '4':
                print("Exiting...")
                break
            else:
                print("Error: Invalid choice. Please try again.")
    except KeyboardInterrupt:
        print("\nOperation interrupted by the user.")
    except (ValueError, IOError) as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
    sys.exit(0)

