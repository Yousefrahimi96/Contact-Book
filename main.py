class ContactBook:
    """A class to manage a contact book with basic CRUD operations."""

    def __init__(self):
        """Initialize an empty contact dictionary."""
        self.contact = {}

    def add_contact(self, name, number, email):
        """Add a new contact to the contact book."""
        if name not in self.contact:
            self.contact[name] = {"number": number, "email": email}
        else:
            print("Name already exists")

    def detect_contact(self, name):
        """Detect and display a contact by name."""
        if name in self.contact:
            info = self.contact[name]
            print(f"Name: {name}")
            print(f"Number: {info['number']}")
            print(f"Email: {info['email']}")
        else:
            print(f"{name} does not exist")

    def update_contact(self, name, number=None, email=None):
        """Update the phone number or email of an existing contact."""
        if name in self.contact:
            if number:
                self.contact[name]['number'] = number
            if email:
                self.contact[name]['email'] = email
        else:
            print(f"{name} does not exist")

    def view_contact(self):
        """Display all contacts in the contact book."""
        for name, info in self.contact.items():
            print(f"Name: {name}")
            print(f"Number: {info['number']}")
            print(f"Email: {info['email']}")

    def delete_contact(self, name):
        """Delete a contact by name."""
        if name in self.contact:
            del self.contact[name]
            print(f"{name} successfully deleted")
        else:
            print(f"{name} not found")


if __name__ == "__main__":
    book = ContactBook()

    while True:
        print("\n--- Contact Book Application ---")
        print("1. Add contact")
        print("2. Detect contact")
        print("3. Edit contact")
        print("4. View contacts")
        print("5. Delete contact")
        print("6. Quit")
        user_choice = input("\nPlease choose an option: ")

        if user_choice == '1':
            name = input("\nEnter Contact name: ")
            number = input("Enter Contact number: ")
            email = input("Enter Contact email: ")
            book.add_contact(name, number, email)

        elif user_choice == '2':
            name = input("\nEnter name of the contact to detect: ")
            book.detect_contact(name)

        elif user_choice == '3':
            name = input("\nEnter name of the contact to edit: ")
            number = input("Enter new/updated phone number or press Enter to keep unchanged: ")
            email = input("Enter new/updated email or press Enter to keep unchanged: ")
            book.update_contact(name, number if number else None, email if email else None)

        elif user_choice == '4':
            print("\nList of Contacts:")
            book.view_contact()

        elif user_choice == '5':
            name = input("\nEnter name of contact to delete: ")
            book.delete_contact(name)

        elif user_choice == '6':
            print("\nThank you for using Contact Book Application. Goodbye!")
            break

        else:
            print("\nInvalid choice! Please try again.")