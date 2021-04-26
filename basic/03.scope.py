#scope
def say_hi():
    name = "Sam"
    print('Hello', name)
def say_bye():
    name = "Tom"
    print("Good bye", name)
say_hi()
say_bye()

def person():
    global surName
    surName = "Smith"
    print('My surname is', surName)

PI = 3.14

def get_circle_square(radius):
    
    print('Square circle with radius', radius, 'eqquall', PI * radius*radius)

get_circle_square(50)