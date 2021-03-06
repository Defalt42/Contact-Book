from Contact import Contact

class ContactBook:

    contacts = []

    def add_contact(self):
        print("Please enter contact information")
        first_name = input("First name: ")
        last_name = input("Last name: ")
        phone = input("Phone: ")
        email = input("Email: ")

        new_contact = Contact(first_name, last_name, phone, email)

        self.contacts.append(new_contact)

    # TODO: Create remove_contact() function

    def remove_contact():
        print("Enter a contact ID. You can find this by displaying all contacts.")
        contact_id = int(input(">> "))


    # TODO: Create update_contact() function

    def display_contacts(self):
        for contact in self.contacts:
            info = contact.get_info()

            print("**********")
            print(contact.get_name())
            print("**********")

            print("ID: " + str(info["id"]))
            print("First name: " + info["first_name"])
            print("Last name: " + info["last_name"])
            print("Phone: " + info["phone"])
            print("Email: " + info["email"])

            print("============================")