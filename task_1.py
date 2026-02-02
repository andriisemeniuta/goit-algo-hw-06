# # class User:
# #     def __init__(self, username):
# #         self.username = username
# #         self.is_admin = False  # По умолчанию никто не админ

# #     def login(self):
# #         return f"Пользователь {self.username} вошел в систему"

# # class Admin(User):
# #     def __init__(self, username, access_key):
# #         # 1. Вызываем родителя через super(), чтобы он записал имя и статус False
# #         super().__init__(username)

# #         # 2. Добавляем админские "фишки"
# #         self.access_key = access_key
# #         self.is_admin = True  # Перезаписываем статус на True

# #     def delete_system(self):
# #         return f"ВНИМАНИЕ: {self.username} удаляет базу данных ключом {self.access_key}!"

# # # Проверка на твоем MacBook:
# # simple_user = User("Andrej")
# # god_mode = Admin("Boss_Andrej", "SECRET_777")

# # print(simple_user.login())    # Просто вошел
# # print(god_mode.login())       # Тоже может входить (наследует метод)
# # print(god_mode.delete_system()) # А это умеет только админ

# class User:
#     def __init__(self, username):
#         self.username = username
#         self.is_admin = False
#     def login(self):
#         return f"polzovatel {self.username} voshel v sistemu"

# class Admin(User):
#     def __init__(self, username, access_key):
# #         super().__init__(username)
# #         self.access_key = access_key
# #         self.is_admin = True
# #     def delete_system(self):
# #         return f"vnimanie {self.username} udalaet sistemu kluchom {self.access_key}"

# # simple_user = User("Andrey")
# # god_mode = Admin("Boss", "secret_777")

# # print(simple_user.login())
# # print(god_mode.login())
# # print(god_mode.delete_system())


# # class A:
# #     pass

# # class B(A):
# #     pass

# # class C(A):
# #     pass

# # class D(B, C):
# #     pass

# # print(D.mro())  # Виведе порядок розв'язання методів для класу D

# # class A:
# #     name = "Я клас A"

# # class B:
# #     name = "Я клас B"
# #     property = "Я знаходжусь в класі B"

# # class C(A, B):
# #     property = "Я знаходжусь в класі C"

# # c = C()
# # print(c.name)
# # print(c.property)

# # # Разные классы с одинаковым методом
# # class SQL_Scanner:
# #     def scan(self):
# #         return "Проверка на SQL-инъекции..."

# # class Port_Scanner:
# #     def scan(self):
# #         return "Сканирование открытых портов..."

# # # Полиморфизм в действии:
# # scanners = [SQL_Scanner(), Port_Scanner()]

# # for s in scanners:
# #     print(s.scan()) # Мы просто говорим "сканируй", и каждый делает это по-своему

# # def start_attack(hacker_tool):
# #     # Нам не важно, ЧТО это за инструмент.
# #     # Главное, чтобы у него был метод .attack()
# #     print(hacker_tool.attack())

# # class Virus:
# #     def attack(self):
# #         return "Файлы зашифрованы!"

# # class Exploit:
# #     def attack(self):
# #         return "Доступ к системе получен!"

# # class MyGrandma:
# #     def attack(self):
# #         return "Бьет внука тапком за хакерство"

# # # Python выполнит всё, потому что у всех есть метод attack()!
# # start_attack(Virus())
# # start_attack(Exploit())
# # start_attack(MyGrandma())


# # items = ["asdad", "asdadaa", "33222", 22, 22111, 21121212]
# # for i, value in enumerate(items):
# #     print(value)

# # from collections import UserDict

# # class MyDictionary(UserDict):
# #     # Приклад додавання нового методу
# #     def add_key(self, key, value):
# #         self.data[key] = value

# # # Створення екземпляра власного класу
# # my_dict = MyDictionary({'a': 1, 'b': 2})
# # my_dict.add_key('c', 3)
# # print(my_dict)

# # my_dict1 = MyDictionary({"c": 22, "x": 332})
# # my_dict1.add_key("zxc", "das")
# # print(my_dict1)

# from collections import UserDict

# contacts = [
#     {
#         "name": "Allen Raymond",
#         "email": "nulla.ante@vestibul.co.uk",
#         "phone": "(992) 914-3792",
#         "favorite": False,
#     },
#     {
#         "name": "Chaim Lewis",
#         "email": "dui.in@egetlacus.ca",
#         "phone": "(294) 840-6685",
#         "favorite": False,
#     },
#     {
#         "name": "Kennedy Lane",
#         "email": "mattis.Cras@nonenimMauris.net",
#         "phone": "(542) 451-7038",
#         "favorite": True,
#     }
# ]

# class Customer(UserDict):
#     def phone_info(self):
#         name = self.get("name").upper()
#         phone = self.get("phone")
#         return f"{name}: {phone}"

#     def email_info(self):
#         return f"{self.get('name')}: {self.get('email')}"

# if __name__ == "__main__":
#     customers = [Customer(el) for el in contacts]

#     print("---------------------------")

#     for customer in customers:
#         print(customer.phone_info())

#     print("---------------------------")

#     for customer in customers:
#         print(customer.email_info())


# from dataclasses import dataclass

# @dataclass
# class Rectangle:
#     width: int
#     height: int

#     def area(self) -> int:
#         return self.width * self.height

# rect1 = Rectangle(10, 5)
# rect2 = Rectangle(7, 3)
# rect3 = Rectangle(8, 6)

# print(f"Площа прямокутника 1: {rect1.area()}")
# print(f"Площа прямокутника 2: {rect2.area()}")
# print(f"Площа прямокутника 3: {rect3.area()}")

# from enum import Enum


# class Day(Enum):
#     MONDAY = 1
#     TUESDAY = 2
#     WEDNESDAY = 3


# day_from_value = Day(1)
# print(day_from_value)

# from enum import Enum, auto

# class OrderStatus(Enum):
#     NEW = auto()
#     PROCESSING = auto()
#     SHIPPED = auto()
#     DELIVERED = auto()

# class Order:
#     def __init__(self, name: str, status: OrderStatus):
#         self.name = name
#         self.status = status

#     def update_status(self, new_status: OrderStatus):
#         self.status = new_status
#         print(f"Замовлення '{self.name}' оновлено до статусу {self.status.name}.")

#     def display_status(self):
#         print(f"Статус замовлення '{self.name}': {self.status.name}.")

# order1 = Order("Ноутбук", OrderStatus.NEW)
# order2 = Order("Книга", OrderStatus.NEW)

# order1.display_status()
# order2.display_status()

# order1.update_status(OrderStatus.PROCESSING)
# order2.update_status(OrderStatus.SHIPPED)

# order1.display_status()
# order2.display_status()

# class Owner:
#     def __init__(self, name: str, phone: str, ves: float):
#         self.name = name
#         self.phone = phone
#         self.ves = ves

#     def info(self):
#         return f"{self.name}: {self.phone}, {self.ves}"

# class Cat:
#     def __init__(self, nickname: str, age: int, owner: Owner, rost: int):
#         self.nickname = nickname
#         self.age = age
#         self.owner = owner
#         self.rost = rost

#     def get_info(self):
#         return f"Cat Name: {self.nickname}, Age: {self.age}, rost1: {self.rost}"

#     def sound(self):
#         return "Meow"

# owner = Owner("Boris", "+380503002010", 3.14)
# cat = Cat("Simon", 4, owner, 33)

# print(cat.owner.info())
# print(cat.get_info())

# class NameTooShortError(Exception):
#     pass

# class NameStartsFromLowError(Exception):
#     pass

# def enter_name():
#     name = input("Enter name: ")
#     if len(name) < 2:
#         raise NameTooShortError("Name is too short, need more than 2 symbols")
#     if not name[0].isupper():
#         raise NameStartsFromLowError("Name should start from capital letter")
#     return name

# if __name__ == "__main__":
#     try:
#         name = enter_name()
#         print(f"Hello, {name}")
#     except (NameTooShortError, NameStartsFromLowError) as e:
#         print(e)


# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass

#     def change_weight(self, new_weight):
#         self.weight = new_weight


# animal = Animal("Simon", 10)
# animal.change_weight(12)
# print(animal.weight)


# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def change(self, newage):
#         self.age = newage


# cat = Animal("bars", 22)
# cat.change(44)


# print(cat.age)

# class Animal:
#     color = "white"

#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass

#     def change_weight(self, weight):
#         self.weight = weight

#     def change_color(self, color):
#         Animal.color = color

# first_animal = Animal("dasd", 3)
# second_animal = Animal("adf", 33)

# first_animal.change_color("red")

# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass

#     def change_weight(self, weight):
#         self.weight = weight

# class Cat(Animal):
#     def say(self):
#         return "Meow"

# cat = Cat("Simon", 10)

# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass

#     def change_weight(self, weight):
#         self.weight = weight


# class Dog(Animal):
#     def __init__(self, nickname, weight, breed):
#         super().__init__(nickname, weight)
#         self.breed = breed


#     def say(self):
#         return "Woof"

# dog = Dog("Barbos", 23, "labrador")

# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass

#     def change_weight(self, weight):
#         self.weight = weight


# class Owner:
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.adress = address

#     def info(self):
#         return {
#             "name": self.name,
#             "age": self.age,
#             "adress": self.adress
#             }


# class Dog(Animal):
#     def __init__(self, nickname, weight, breed, owner):
#         self.breed = breed
#         self.owner = owner

#         super().__init__(nickname, weight)

#     def say(self):
#         return "Woof"

#     def who_is_owner(self):
#         return self.owner.info()


class A:
    x = "I am A class"


class B:
    x = "I am B class"
    y = "I exist only in B"


class C(A, B):
    z = "This exists only in C"


c = C()
# print(c.z)  # This exists only in C
# print(c.y)  # I exist only in B
# print(c.x)  # I am A class

# print(C.mro())

# class A:
#     x = 'I am A class'


# class B:
#     x = 'I am B class'
#     y = 'I exist only in B'


# class C(B, A):
#     z = "This exists only in C"


# c = C()
# print(c.z)  # This exists only in C
# print(c.y)  # I exist only in B
# print(c.x)  # I am B class

# print(C.mro())

# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass

#     def info(self):
#         return f"{self.nickname}-{self.weight}"


# class Cat(Animal):
#     def say(self):
#         return "Meow"


# class Dog(Animal):
#     def say(self):
#         return "Woof"

# class CatDog(Cat, Dog):
#     pass

# class DogCat(Dog, Cat):
#     pass

# dc = DogCat("dasd", 11)
# print(dc.say())


# from collections import UserDict

# class LookUpKeyDict(UserDict):
#     def lookup_key(self, value):
#         keys = []
#         for k, v in self.data.items():
#             if v == value:
#                 keys.append(k)
#         return keys

# from collections import UserList


# class AmountPaymentList(UserList):
#     def amount_payment(self):
#         total = 0
#         for value in self.data:
#             # if value > 0:
#                 total = total + value
#         return total
    
# payments = AmountPaymentList([100, -300, 400])
# pay1 = AmountPaymentList([100, 200])
# print(payments.amount_payment())
# print(pay1.amount_payment())



















