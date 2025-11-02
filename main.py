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
        if not self._is_valid(value):
            raise ValueError('Phone should contain 10 digits!')
        super().__init__(value)
        
    @staticmethod
    def _is_valid(value: str) -> bool:
        return value.isdigit() and len(value) == 10

class Record:
    def __init__(self, name: str, phones = None):
        self.name = Name(name)
        self.phones = phones if phones else []
    
    def add_phone(self, phone: str):
           self.phones.append(Phone(phone))

    def remove_phone(self,phone_value: str):
           self.phones = [p for p in self.phones if p.value != phone_value] 

    def edit_phone(self,old_value: str, new_value: str):
        for phone in self.phones:
            if phone.value == old_value:

                if not Phone._is_valid(new_value):
                    raise ValueError('Phone should contain 10 digits!')
                
                phone.value = new_value
                return True
        return False
        
    def find_phone(self, phone_value: str):
        for phone in self.phones:
            if phone.value == phone_value:
                  return phone
        return 'No phone found!'
              

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str) -> Record:
        record = self.data.get(name)
        if record is None:
            raise KeyError (f'No record found for {name}.')
        return record
    
    def delete(self,name:str):
        if name in self.data:
            del self.data[name]      


if __name__ == '__main__':

# Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")
