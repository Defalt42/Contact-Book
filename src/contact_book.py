from Contact import Contact

contacts = []

def add_contact():
    print("Please enter contact information")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    phone = input("Phone: ")
    email = input("Email: ")

    new_contact = Contact(first_name, last_name, phone, email)

    contacts.append(new_contact)

def display_contacts():
    for contact in contacts:
        info = contact.get_info()

        print("**********")
        print(contact.get_name())
        print("**********")

        print("First name: " + contact.first_name)
        print("Last name: " + contact.last_name)
        print("Phone: " + contact.phone)
        print("Email: " + contact.email)

        print("============================")