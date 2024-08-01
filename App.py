# Simple Address Book:

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self,name}, {self.phone}, {self.email}"

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact {contact.name} added.")

    def remove_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Contact {name} removed.")
                return
            print(f"Contact {name} not found.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Address Book")
            for contact in self.contacts:
                print(contact)

address_book = AddressBook()
while True:
    print("\n1. Add Contact\n2. Remove Contact\n3. View Contacts\n4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter your name: ")
        phone = input("Enter your phone: ")
        email = input("Enter your email: ")
        contact = Contact(name, phone, email)
        address_book.add_contact(contact)
    elif choice == "2":
        name = input("Enter your name: ")
        address_book.remove_contact(name)
    elif choice == "3":
        address_book.view_contacts()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")