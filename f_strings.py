person = "Dave"
coins = 3

print("\n" + person + " has " + str(coins) + " coins left.")

message = "\n%s has %s coins left." % (person, coins)
print(message)

message = "\n{} has {} coins left.".format(person, coins)
print(message)

message = "\n{1} has {0} coins left.".format(person, coins)
print(message)

message = "\n{person} has {coins} coins left.".format(person=person, coins=coins)
print(message)


#f-string
message = f"\n {person} has {coins} coins left."

for num in range(1,12):
    print(f"\n2.25 times {num} is {2.25 * num:.2f}")