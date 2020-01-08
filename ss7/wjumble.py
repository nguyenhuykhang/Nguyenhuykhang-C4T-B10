import random
item = ['red', 'yellow', 'blue','black','grey']

n = int(input("Chon mot so tu 0 den 4: "))

s = list(item[n])

random.shuffle(s)
print(*s)

l = str(input("Nhap vao tu do: "))

while True:
    if l == item[n]:
        print("Chinh xac!!")
        break
    else:
        print("Khong chinh xac")
     