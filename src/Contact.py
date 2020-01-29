class Contact:
    def __init__(self, first_name, last_name, phone=None, email=None):
        self.id = id(self)
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
    
    def get_name(self):
        return self.first_name + ' ' + self.last_name
    
    def get_info(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone": self.phone,
            "email": self.email
        }
    
    def set_email(self, new_email):
        self.email = new_email
    
    def set_phone(self, new_phone):
        self.phone = new_phone
    