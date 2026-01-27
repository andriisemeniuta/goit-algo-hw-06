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
#         super().__init__(username)
#         self.access_key = access_key
#         self.is_admin = True
#     def delete_system(self):
#         return f"vnimanie {self.username} udalaet sistemu kluchom {self.access_key}"

# simple_user = User("Andrey")
# god_mode = Admin("Boss", "secret_777")

# print(simple_user.login())
# print(god_mode.login())
# print(god_mode.delete_system())


# class A:
#     pass

# class B(A):
#     pass

# class C(A):
#     pass

# class D(B, C):
#     pass

# print(D.mro())  # Виведе порядок розв'язання методів для класу D

# class A:
#     name = "Я клас A"

# class B:
#     name = "Я клас B"
#     property = "Я знаходжусь в класі B"

# class C(A, B):
#     property = "Я знаходжусь в класі C"

# c = C()
# print(c.name)
# print(c.property)

# # Разные классы с одинаковым методом
# class SQL_Scanner:
#     def scan(self):
#         return "Проверка на SQL-инъекции..."

# class Port_Scanner:
#     def scan(self):
#         return "Сканирование открытых портов..."

# # Полиморфизм в действии:
# scanners = [SQL_Scanner(), Port_Scanner()]

# for s in scanners:
#     print(s.scan()) # Мы просто говорим "сканируй", и каждый делает это по-своему

def start_attack(hacker_tool):
    # Нам не важно, ЧТО это за инструмент. 
    # Главное, чтобы у него был метод .attack()
    print(hacker_tool.attack())

class Virus:
    def attack(self):
        return "Файлы зашифрованы!"

class Exploit:
    def attack(self):
        return "Доступ к системе получен!"

class MyGrandma:
    def attack(self):
        return "Бьет внука тапком за хакерство"

# Python выполнит всё, потому что у всех есть метод attack()!
start_attack(Virus())
start_attack(Exploit())
start_attack(MyGrandma())




















