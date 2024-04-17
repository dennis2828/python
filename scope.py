name = "Dave"
count = 1

def greeting():
    color = "blue"
    global count
    count+=1
    print(count)

greeting()


print(count)