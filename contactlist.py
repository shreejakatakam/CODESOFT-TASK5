class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address
    
    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone_number}\nEmail: {self.email}\nAddress: {self.address}"

class ContactBook:
    def __init__(self):
        self.contacts = []
    
    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully.")
    
    def view_contacts(self):
        if not self.contacts:
            print("Contact list is empty.")
        else:
            for index, contact in enumerate(self.contacts, start=1):
                print(f"\nContact {index}:")
                print(contact)
    
    def search_contact(self, search_term):
        found = False
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                print(contact)
                found = True
        if not found:
            print("Contact not found.")
    
    def update_contact(self, search_term):
        found = False
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                new_name = input(f"Enter new name for {contact.name}: ").strip()
                new_phone = input(f"Enter new phone number for {contact.name}: ").strip()
                new_email = input(f"Enter new email for {contact.name}: ").strip()
                new_address = input(f"Enter new address for {contact.name}: ").strip()
                
                contact.name = new_name if new_name else contact.name
                contact.phone_number = new_phone if new_phone else contact.phone_number
                contact.email = new_email if new_email else contact.email
                contact.address = new_address if new_address else contact.address
                
                print("Contact updated successfully.")
                found = True
                break
        if not found:
            print("Contact not found.")
    
    def delete_contact(self, search_term):
        found = False
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                found = True
                break
        if not found:
            print("Contact not found.")

def main():
    contact_book = ContactBook()
    
    while True:
        print("\n===== Contact Management System =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            name = input("Enter name: ").strip()
            phone_number = input("Enter phone number: ").strip()
            email = input("Enter email: ").strip()
            address = input("Enter address: ").strip()
            
            new_contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(new_contact)
        
        elif choice == '2':
            contact_book.view_contacts()
        
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ").strip()
            contact_book.search_contact(search_term)
        
        elif choice == '4':
            search_term = input("Enter name or phone number of contact to update: ").strip()
            contact_book.update_contact(search_term)
        
        elif choice == '5':
            search_term = input("Enter name or phone number of contact to delete: ").strip()
            contact_book.delete_contact(search_term)
        
        elif choice == '6':
            print("Exiting Contact Management System.")
            break
        
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
