class Person:
    def __init__(self, name):
        self.__name = name
        self.__age = 1
        
    @property
    def age(self):
        return self.__age
            
    @age.setter
    def age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            print("Не доступный возраст")
    
    @property
    def name(self):
        return self.__name
        
    def display_info(self):
        print("Name:", self.__name, "\tAge:", self.__age)

tom = Person("Tom")

tom.display_info()
tom.age = -85528
print(tom.age)
tom.age = 36
tom.display_info()