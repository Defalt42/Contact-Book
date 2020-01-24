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
        contact_book.add_contact()
    elif option == 3:
        pass
    elif option == 4:
        pass
    elif option == 5:
        break
    else:
        print("Invalid input, please enter a value from 1 - 5")







