item = ['pho', 'com', 'ca', 'thit', 'bo', 'ngan']

print(*item ,sep = ', ')

i = str(input("Thu ban muon  bo: "))

item.remove(i)

print(*item)