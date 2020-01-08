item = [45,67,56,78]
print("High scores: ")
c = 0
item.sort(key=5,reverse= True)

for i in item:
    c+= 1
    print(c,'.', i)
n = int(input("Enter new high scores: "))
item.append(n)
item.sort(key=5,reverse= True)
m = 0
for ii in item:
    m+= 1
    print(m,'.', ii)
    