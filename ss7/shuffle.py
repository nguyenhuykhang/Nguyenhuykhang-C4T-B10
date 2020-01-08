import random

n = str(input("Nhap vao mot tu: "))


print(n)
s = list(n)

random.shuffle(s)

for i in s:
    print(i)