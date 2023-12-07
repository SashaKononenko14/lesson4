#Наслідування класів
class Grandparents:
    height = 170
    eyes = "green"
    age = 70
class Parent(Grandparents):
    pass
    age = 40
class Child(Parent):
    pass
    age = 15
    height = 165
    def __init__(self):
        print(self.height)
        print(self.eyes)
        print(self.age)

max = Child()
#приклад
class Human:
    height = 170
class Student(Human):
    pass
class Worker(Human):
    pass

nick = Student()
kate = Worker()
print(nick.height, kate.height)