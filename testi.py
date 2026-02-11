from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if not (len(value) == 10 and value.isdigit()):
            raise ValueError("Invalid phone format")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number):
        for p in self.phones:
            if p.value == phone_number:
                self.phones.remove(p)
                return

    def edit_phone(self, old_number, new_number):
        new_phone = Phone(new_number)
        for i, p in enumerate(self.phones):
            if p.value == old_number:
                self.phones[i] = new_phone
                return
        raise ValueError("Phone not found")

    def find_phone(self, phone_number):
        for p in self.phones:
            if p.value == phone_number:
                return p
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise ValueError("Invalid дата")

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())



adbook = AddressBook()

cont = Record("Andrey")
cont1 = Record("oleg")
cont2 = Record("vasya")
cont.add_phone("0987654321")
cont.add_phone("0987651234")
cont.remove_phone("0987654321")
cont.edit_phone("0987651234", "0987651562")


adbook.add_record(cont)
adbook.add_record(cont1)
adbook.delete("oleg")




# print(cont)
print(adbook)

















# book = AddressBook()

# john_record = Record("John")
# john_record.add_phone("1234567890")
# book.add_record(john_record)
# print(book)







































