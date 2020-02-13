from Contact import Contact

class ContactBook:

    contacts = []

    def get_contact(self, id):
        pass

    def add_contact(self, first, last, phone, email):
        self.contacts.append(Contact(first, last, phone, email))    

    def remove_contact(self, contact_id):

        for contact in self.contacts:
            if int(id(contact)) == contact_id:
                self.contacts.remove(contact)
                return True
        return False
        

    # TODO: Create update_contact() function
    def update_contact(self, key, value):
        pass

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