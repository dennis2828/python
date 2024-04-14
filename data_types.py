import math


# String data type

# literal assignment
first = "Dennis"
last = "Moldovan"

# print(type(first), type(last))

# print(type(last))
# print(isinstance(last, str))
# print(isinstance(last, str))

# print("#####")
# #constructor function
# pizza = str("Pepperoni")
# print(type(pizza)==str)
# print(isinstance(pizza, str))


# Concatenation
fullname = str(first + " " + last)

print(fullname)

fullname+="!"
print(fullname)

# Casting a number to a string
decade = str(1980)
print(type(decade))
decade+="!"
print(decade)

multiline = '''
    Hey, how are u?
    I was just checking in.

            all good good?

'''
print(multiline)

sentence = 'I\'m back at work!\tHey!\n\nWhere\'s at\\located2?'
print(sentence)

#string methods

print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)


print(len(multiline))
multiline += "                                               "
multiline = "            " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print("")
# Build a menu
title = "menu".upper()
print(title.center(22, "="))
print("Coffe".ljust(16, ".")+"$1".rjust(4))
print("Muffin".ljust(16, ".")+"$1".rjust(4))
print("Cheesecake".ljust(16, ".")+"$1".rjust(4))
print("")
# string index values
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

# Some methods return boolean data
print(first.startswith("D"))
print(first.endswith("s"))


# Boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(x, bool))


# Numeric data types
# integer type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

#float type

gpa = 3.28
y = float(1.14)
print(type(gpa))
print(isinstance(gpa, float))

# complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real, comp_value.imag)

print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))

print(round(gpa, 1))

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# Casting a string to a number
zipcode = "10001"
zip_value = int(zipcode)
print(zip_value)

# Error if u attempt to cast incorrect data