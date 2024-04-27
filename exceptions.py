class JustNotCoolError(Exception):
    pass

x=2

try:
    # print(x/0)
    raise JustNotCoolError("This isnt a cool eror")
    raise Exception("I'm a custom exception")
    if not type(x) is str:
        raise TypeError("Only strings are allowed")
except NameError:
    print("there is an error")
except ZeroDivisionError:
    print("divison by 0")
except Exception as error:
    print(error)
finally:
    print("I'm going to print with or withou error")