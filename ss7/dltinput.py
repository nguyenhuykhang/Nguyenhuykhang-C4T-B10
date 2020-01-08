item = ['pho', 'com', 'ca', 'thit', 'bo', 'ngan']

print(*item ,sep = ', ')

i = int(input("Thu ban muon  bo, nhap so thu tu: "))

item.pop(i)

print(item)