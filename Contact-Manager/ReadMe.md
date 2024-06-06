## Documentation : Contact Manager

### Overview
This Python script provides a command-line interface for managing contacts. Users can add, delete, and display contacts, which are stored in a JSON file. The script ensures data integrity by handling exceptions and providing user-friendly error messages.

### Requirements
- Python 3.x

### Usage
1. Run the script and follow the menu prompts to add, delete, or display contacts.
2. The contacts are saved in a JSON file named `contacts.json` in the current directory.

### Implementation Details
#### Class: `ContactManager`
- Manages contacts stored in a JSON file.
- Methods:
  - `__init__(self, filename)`: Initializes the ContactManager object with the filename of the JSON file containing contacts.
  - `load_contacts(self)`: Loads contacts from the JSON file.
  - `save_contacts(self)`: Saves contacts to the JSON file.
  - `add_contact(self, name, phone, email)`: Adds a new contact with the specified name, phone number, and email address.
  - `delete_contact(self, index)`: Deletes the contact at the specified index.
  - `display_contacts(self)`: Displays all contacts stored in the ContactManager object.

#### Function: `main()`
- Provides a menu-driven interface for interacting with the ContactManager.
- Options:
  - `1. Add Contact`: Prompts the user to enter details of a new contact and adds it to the contact list.
  - `2. Delete Contact`: Prompts the user to enter the index of the contact to delete and removes it from the contact list.
  - `3. Display Contacts`: Displays all contacts stored in the contact list.
  - `4. Exit`: Exits the program.

### Conclusion
This script provides a simple and efficient way to manage contacts through a command-line interface. It can be easily integrated into other applications or extended with additional features as needed. The use of a JSON file for storage ensures data persistence and portability across different platforms.

## **License**
This project is licensed under the MIT License. See the [LICENSE](https://github.com/kavineksith/Automating-Daily-IT-Operations-with-Python-Integration/blob/main/LICENSE) file for details.

### **Disclaimer:**
Kindly note that this project is developed solely for educational purposes, not intended for industrial use, as its sole intention lies within the realm of education. We emphatically underscore that this endeavor is not sanctioned for industrial application. It is imperative to bear in mind that any utilization of this project for commercial endeavors falls outside the intended scope and responsibility of its creators. Thus, we explicitly disclaim any liability or accountability for such usage.