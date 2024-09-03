contacts = []
def add_contact(name, phone, email):
    contact = {'Name': name, 'Phone': phone, 'Email': email}
    contacts.append(contact)
    print(f"Contact {name} added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
        return
    for contact in contacts:
        print(f"Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}")


def search_contact(name):
    for contact in contacts:
        if contact['Name'].lower() == name.lower():
            print(f"Found contact: Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}")
            return
    print(f"No contact found with the name {name}.")

def update_contact(name, phone=None, email=None):
    for contact in contacts:
        if contact['Name'].lower() == name.lower():
            if phone:
                contact['Phone'] = phone
            if email:
                contact['Email'] = email
            print(f"Contact {name} updated successfully.")
            return
    print(f"No contact found with the name {name}.")

def main():
    while True:
        print("\nContact Management System")
        print("\n1.Add Contact")
        print("\n2.View Contact")
        print("\n3.Search Contact")
        print("\n4.Update Contact")
        print("\n5.Exit")

        choice = input("Please Enter Your Choice: ")
        if choice =='1':
            name=input("Enter Your Name: ")
            phone=input("Enter Your Phone Number: ")
            email=input("Enter Your Email: ")
            add_contact(name,phone, email)

        elif choice=='2':
            view_contacts()

        elif choice=='3':
            name = input("Enter the name of the contact to search: ")
            search_contact(name)

        elif choice=='4':
            name = input("Enter the name of the contact to update: ")
            phone = input("Enter new phone number (leave empty if no change): ")
            email = input("Enter new email (leave empty if no change): ")
            update_contact(name, phone if phone else None, email if email else None)

        elif choice=='5':
            print("Exiting...")
            break

        else:
            print("Invalid Choice.\nPlease Enter Valid Choice")
main()