from collections import UserDict

class Field:    
    def __init__(self, value):
        self.value = value

class Phone(Field):     
     pass
    
class Name(Field):
     pass

class Email(Field):
    pass

class Record:
    def __init__(self, name: str, phones: list, emails: list):
        self.name = name
        self.phones = [phones]
        self.emails = [emails]
        
    def add_phone(self, phone):
        phone_number = Phone(phone)
        if phone_number not in self.phones:
            self.phones.append(phone_number)

    def add_email(self, email):
        email_adress = Email(email)
        if email_adress not in self.emails:
            self.emails.append(email_adress)

    def find_phone(self, value):
        pass

    def delete_phone(self, phone):
        if phone in self.phones:
            index = self.phones.index(phone)
            self.phones.remove(phone)
            return index
        else:
            return None

    def edit_phone(self, old_phone, new_phone):
        if old_phone in self.phones:
            index = self.phones.index(old_phone)
            self.phones[index] = new_phone
            return index
        else:
            return None


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find_record(self, value):
        return self.data.get(value)
    
if __name__ == '__main__':
    name = Name('Bill')
    phone = Phone('1234567890')
    email = Email('bill@gmail.com')
    rec = Record(name, phone, email)
    ab = AddressBook()
    ab.add_record(rec)
    
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)

    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'

    assert isinstance(ab['Bill'].emails, list)
    assert isinstance(ab['Bill'].emails[0], Email)
    assert ab['Bill'].emails[0].value == 'bill@gmail.com'
    
    print('All Ok)')