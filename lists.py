users = ["Dingo", "Dennis"]
data = ["Dingo", 42, True]

empty_list = []

print("Dingo" in empty_list)
print(users[0])
print(users[-1])

print(users.index("Dennis"))

print(users[0: 1])
print(users[-1:])

print(len(data))

users.append("Elsa")

print(users)
print(len(users))

users += ["Jason"]
print(users)

users.extend(["Robert", "Ice"])
print(users)

# users.extend(data)
# print(users)

users.insert(0, "Bob")
print(users)

users[2:2] = ["Eddie", "Alex"]
print(users)


users[1:3] = ["Robert", "JPJ"]
print(users)

users.remove("Bob")
print(users)

print(users.pop())

del users[1]
print(users)

# del data
data.clear()
print(data)

users[1:2] = ["dave"]
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [4, 42, 78, 1, 5]

nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)
print(sorted(nums, reverse=True))

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]


mytuple = tuple(("Dave",42,True))
anothertuple = (1,4,2,8)
print(mytuple)
print(type(mytuple))
print(isinstance(mytuple, tuple))

newlist = list(mytuple)
newlist.append("Neil")
newtuple = tuple(newlist)
print(newtuple)

(one, two, *hey) = anothertuple
print(one, two, hey)

print(anothertuple.count())