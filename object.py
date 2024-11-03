# class dog:
#     pass
#
# dog = dog()
# dog.name = "olivia"
# dog.birth_year = 1999
#
#
# print(f"{dog.name:s} was born in {dog.birth_year:d}")
#
# class visitor:
#     def __init__(self, name: str, height: int):
#         self.name = name
#         self.height = height
#
# class atractons:
#     def __init__(self, name:str, min_height:int):
#         self.visitor_num = 0
#         self.name = name
#         self.min_height = min_height
#
#     def check_height(self, person:visitor):
#         if person.height >= self.min_height:
#             self.visitor_num += 1
#             print(f"{person.name}: welcome, you're in")
#         else:
#             print(f"{person.name}: not enough height")
#
#     def __str__(self):
#         return f"{self.name} ({self.visitor_num} visitors)"
#
# helicopter = atractons("Helicopter", 120)
# Emma = visitor("Emma", 130)
# Semma = visitor("Semma", 140)
# Gemma = visitor("Gemma", 150)
# Hemma = visitor("Hemma", 100)
# Temma = visitor("Temma", 120)
#
# helicopter.check_height(Emma)
# helicopter.check_height(Semma)
# helicopter.check_height(Gemma)
# helicopter.check_height(Hemma)
# helicopter.check_height(Temma)
#
# print(helicopter.name)
#
#
#
#
#
#
# class student:
#     def __init__(self, name:str, age:int, height:int):
#         self.name = name
#         self.age = age
#         self.height = height
#
# megha = student("mahi", 19, 5)
# mahi = student("megha", 19, 6)
#
# print(f" The name of {megha.name:s} has height of {megha.height:d} at the age of {megha.age:d}")
# print(f" The name of {mahi.name:s} has height of {mahi.height:d} at the age of {mahi.age:d}")

class Dog:
    def __init__(self, name:str, birth_year:int, sound:"woot woot"):
        self.name = name
        self.birth_year = birth_year
        self.sound = sound

    def bark(self, times):
        for i in range(times):
            print(self.sound)
        return

dog1 = ("doggy", 1999)
dog2 = ("dogy", 1990, "yup yup yup")

dog1.bark(2)
dog2.bark(6)









