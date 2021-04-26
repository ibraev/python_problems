class Person:
    def __init__(self, name):
        self.name = name
    def display_info(self):
        print('Hello, my name is', self.name)

person1 = Person("Tom")
person1.display_info()

person2 = Person("Sam")
person2.display_info()