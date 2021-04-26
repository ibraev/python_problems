intNumber = 1;

strName = 'My name is Iskender'

strLastName = 'Ibraev'

pi = 3.14

listArray = [1,2,3,4,5,6,7,8,9]
mapped_numbers = list(map(lambda x: x * 2 + 3,  listArray))
print(mapped_numbers)

status = False

z = complex(2, -3)
print(z)

def displayInfo():
    print('Name:', strName, '\t', "Age:", age )
displayInfo

def sum(*params):
    result = 0
    for n in params:
        result += n
    return result
sumOfNumbers1 = sum(1, 2, 3, 5)
sunOfNumbers2 = sum(3, 4, 6)

print(sumOfNumbers1)
print(sunOfNumbers2)

def exchange(usdRate, money):
    result = round(money/usdRate, 2)
    return result
    
result1 = exchange(60, 30000)
print(result1)
result2 = exchange(56, 30000)
print(result2)
result3 = exchange(65, 3000)
print(result3)


