squared = lambda num : num*num

print(squared(2))

addTwo = lambda num : num+2


def funcBuilder(x):
    return lambda num : num+x

addTen = funcBuilder(10)
addTwenty = funcBuilder(20)


print(addTen(7))
print(addTwenty(7))



numbers = [3,7,12,18,20,21]

squared_nums = map(lambda num : num*num, numbers)

print(squared_nums,list(squared_nums))


lambda num : num%2 !=0

odd_nums = filter(lambda num : num%2 !=0, numbers)

print(list(odd_nums))

from functools import reduce

lambda acc, curr : acc + curr

sum_nums = reduce(lambda acc, curr : acc+curr, numbers)

print(sum_nums)