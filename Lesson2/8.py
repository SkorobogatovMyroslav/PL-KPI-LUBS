import random
a = [random.randint(0, 50) for i in range(10)]
print("do:",a)
for i in range(10):
    a[i] *= 2
print("pislya:",a)
