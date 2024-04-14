value = 1

# while value <= 10:
#     print(value)
#     if(value==5):
#         break
#     value+=1


# while value <= 10:
#     value+=1
#     if(value==5):
#         continue
#     print(value)
# else:
#     print("this should be eleven", value)



names = ["Dave", "Sarah", "John"]
# for x in names:
#     print(x)

# for x in "Mississippi":
#     print(x)

# for x in names:
#     if(x=="Sarah"):
#         continue
#     print(x)

# for x in range(4):
#     print(x)
for x in range(0,100,5):
    print(x)
else:
    print(x)
    print("That is over")

actions = ["codes", "eats", "sleeps"]

for name in names:
    for action in actions:
        print(name + " " + action + ".")
    print("")

for action in actions:
    for name in names:
        print(name + " " + action + ".")
    print("")