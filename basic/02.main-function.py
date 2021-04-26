#main-function
def main():
    say_hello("Tom")
    usd_rate = 56
    money = 30000
    result = exchange(usd_rate, money)
    print("You", result, 'dollars')
    
def say_hello(name):
    print('Hello', name)

def exchange(usd_rate, money):
    result = round(money/usd_rate, 2)
    return result
main()

#fuction can return many values
def create_defail_user():
    name="Tom"
    age= 33
    return name, age


user_name, user_age = create_defail_user()
print("Name:", user_name, "\t Age:", user_age)

