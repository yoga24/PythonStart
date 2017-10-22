class Fibonacci:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.b


fib = Fibonacci()
for i in range(10):
    print('Fib : ', next(fib))

# List Compr
print([i ** 2 for i in range(50) if i % 8 == 0])
print([i ** 2 for i in range(50) if i ** 2 % 8 == 0])

# Problem 3 : @12.50 : Multiple List Compr
print([x for x in [i * 2 for i in range(10)] if x % 8 == 0])

# Problem 4 : @13.30 : Multiple List Compr
import random

print([num for num in random.sample(range(1, 1001), 50) if num % 9 == 0])
