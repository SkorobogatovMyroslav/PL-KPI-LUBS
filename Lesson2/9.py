import random
a = [random.randint(0, 50) for i in range(10)]
print(a)
c = 0
for i in a:
    if i % 2 == 0:
        c += 1
print("kilk parn", c)
