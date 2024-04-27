# r = Read
# a = Append
# w = Write
# x = Create


# Read - error if it doesn't exist

f = open("names.txt")

# print(f.read())
# print(f.read(4))

# print(f.readline())
# print(f.readline())


for line in f:
    print(line)

f.close()

try:
    f = open("names.txt")
    print(f.read())
except Exception as error:
    print("The file you want to read doesn't exist")
finally:
    f.close()
print("\n\n\n\n")
f = open("names.txt", "a")

f.write("Neil")
f.close()

f = open("names.txt")
print(f.read())
f.close()


f = open("context.txt","w")
f.write("test")
f.close()

f = open("context.txt")
print(f.read())
f.close()


with open("names.txt") as f:
    print(f.read())