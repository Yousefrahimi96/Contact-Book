class ContactBook:
    def __init__(self):
        self.contact = {}
        
    def add_contact(self, name, number, email):
        
        if name not in self.contact:
            self.contact[name] = {"number" : number, "email" : email}
        else:
            print("name is exist") 
        
    def detect_contact(self, name):
        if name in self.contact:
            info = self.contact[name]
            print(f"Name: {name}")
            print(f"Number: {info['number']}")
            print(f"Email: {info['email']}")
        else:
            print(f"{name} is not exist")
    
    def update_contact(self, name, number= None, email= None):
        if name in self.contact:
            if number is not None:
                self.contact[name]['number'] = number
            if email is not None:
                self.contact[name]['email'] = email
        else:
            print(f"{name} is not exist")
    
    def view_contact(self):
        for name, info in self.contact.items():
            print("Name:", name)
            print("Number:", info['number'])
            print("Email:", info['email'])
        
    def delete_contact(self, name):
        if name in self.contact:
            del self.contact[name]
            print(f"{name} succesfuly deleted")
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
            book.update_contact(name, number or None, email or None)

        elif user_choice == '4':
            print("\nList of Contacts:")
            book.view_contact()

        elif user_choice == '5':
            name = input("\nEnter name of contact to delete: ")
            book.delete_contact(name)

        elif user_choice == '6':
            print("\nThank You for using Contact Book Application. Goodbye!")
            break

        else:
            print("\nInvalid choice! Please try again.")
