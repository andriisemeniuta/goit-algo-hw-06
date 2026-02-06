class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        contact = {
            "id": Contacts.current_id,
            "name": name,
            "phone": phone,
            "email": email,
            "favorite": favorite,
        }
        self.contacts.append(contact)
        Contacts.current_id += 1

    def get_contact_by_id(self, id):
        for contact in self.contacts:
            if contact.get("id") == id:
                return contact
        else:
            return None

    def remove_contacts(self, id):
        for contact in self.contacts:
            if contact.get("id") == id:
                self.contacts.remove(contact)
                break

conts = Contacts()
conts.add_contacts("sasha", "0991112233", "asfsa@sdf.com", True)
conts.add_contacts("nika11", "03333112233", "asfsa@sdf.com", True)
conts.add_contacts("nika22", "03333112233", "asfsa@sdf.com", True)
conts.add_contacts("nika333", "03333112233", "asfsa@sdf.com", True)

print(conts.list_contacts())   
print(len(conts.list_contacts()))   
conts.remove_contacts(1)

print(len(conts.list_contacts()))   














































