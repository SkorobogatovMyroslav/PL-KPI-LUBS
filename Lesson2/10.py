import random
a = [random.randint(0, 50) for i in range(10)]
print(a)
a.insert(0, -1)
print(a)
