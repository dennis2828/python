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