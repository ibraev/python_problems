try:
    number1 = int(input("Enter you first number:"))
    number2 = int(input("Enter you second number"))
    print("Result division", number1/number2)
except ValueError:
       print("Conversion pass error")
except ZeroDivisionError:
    print('Attempt error')
except Exception:
    print("General exception")
print("Finally program")

try: 
    number3 = int(input("Enter you: "))
    print("Enter you number", number3)
except ValueError:
    print("Could not convert number")
finally:
    print("Block try finall completed execution")

try:
    number4 = int(input("Enter you number: "))
    print("Enter you number:", number4)
except ValueError as e:
    print("info", e)
print("Finally program")