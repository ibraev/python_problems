
try:
    somefile = open("hello.text", "w")
    try:
        somefile.write("hello world")
    except Exception as e:
        print(e)
    finally:
        somefile.close()
except Exception as ex:
    print(ex)
    
with open("myfile.txt", "w") as file:
    file.write("hello world")

with open("myfile.txt", "a") as file:
    file.write("\ngood bye, world")

with open("myfile.txt", "a") as hellofile:
    print("Hello, world", file=hellofile)
    
with open("myfile.txt", "r") as file:
    str1 = file.readline()
    print(str1, end="")
    
 