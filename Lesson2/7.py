import random
a = [random.randint(0, 50) for i in range(10)]
print(a)
for i in range(10):
    if a[i] == 0:
        print("Нульовий елемент на індексі:", i)
