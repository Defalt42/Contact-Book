from ContactBook import ContactBook

contact_book = ContactBook()

print("Welcome to PyContacts!")
print("This is a command line contact book program that will help keep track of all your contacts. Here are some options to get started.")

# TODO: Create main menu

while True:
    print("1) List contacts")
    print("2) Add a contact")
    print("3) Remove a contact")
    print("4) Update a contact")
    print("5) Quit")

    option = int(input("What would you like to do? (type a number) >> "))

    if option == 1:
        contact_book.display_contacts()
    elif option == 2:
        first = input("First name >> ")
        last = input("Last name >> ")
        phone = input("Phone number >> ")
        email = input("Email >> ")

        contact_book.add_contact(first, last, phone, email)
    elif option == 3:
        print("Here is a list of all contacts in your contact book.")
        contact_book.display_contacts()

        while True:
            contact_id = int(input("Enter the ID of the contact you would like to remove >> "))
            
            if contact_book.remove_contact(contact_id):
                print("Contact successfully removed!")
                contact_book.display_contacts()
                break
            else:
                print("Contact does not exist. Try again. ")
                contact_book.display_contacts()
                continue
    elif option == 4:
        pass
    elif option == 5:
        break
    else:
        print("Invalid input, please enter a value from 1 - 5")







