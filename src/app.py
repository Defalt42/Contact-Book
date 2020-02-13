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

    try:
        option = int(input("What would you like to do? (type a number) >> "))
    except ValueError:
        print("Oops, invalid input. Try entering an integer.")

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
            try:
                contact_id = int(input("Enter the ID of the contact you would like to remove >> "))
            except ValueError:
                print("Oops, invalid input. Try entering an integer.")
            
            if contact_book.remove_contact(contact_id):
                print("Contact successfully removed!")
                contact_book.display_contacts()
                break
            else:
                print("Contact does not exist. Try again. ")
                contact_book.display_contacts()
                continue
    elif option == 4:
        print("Here is a list of all contacts in your contact book.")
        contact_book.display_contacts()

        while True:
            try:
                contact_id = int(input("Enter the ID of the contact you would like to update >> "))
            except ValueError:
                print("Oops, invalid input. Try entering an integer.")
            
            if contact_book.remove_contact(contact_id):
                print("Contact successfully removed!")
                contact_book.display_contacts()
                break
            else:
                print("Contact does not exist. Try again. ")
                contact_book.display_contacts()
                continue
    elif option == 5:
        break
    else:
        print(str(option) + " is not an option, please enter a value from 1 - 5")







