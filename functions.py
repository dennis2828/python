def hello_world():
    print("Hello World!")

hello_world()

def sum(num1, num2):
    if (type(num1) is not int or type(num2) is not int):
        return
    return num1+num2


print(sum(2,20/8%4))

def multiple_items(*args):
    print(args)
    print(type(args))

multiple_items(1,2,3)

def round(roundCount):
    print(roundCount)