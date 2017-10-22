from functools import reduce


def get_fibonacci(num):
    num1 = 0
    num2 = 1
    aList = [num1, num2]
    while num2 < num:
        aList.append(num2)
        num1, num2 = num2, num1 + num2
    return aList
#9227465
sum = 0
for i in get_fibonacci(4000000):
    if i % 2 == 0:
        sum += i

print(sum)

