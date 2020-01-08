items = ['pho','bun','chao']
for i in range(3):
    fav = input("Nhap vao thu ban muon them: ")
    items.append(fav)
l = len(items)
for i in range(l):

    print(items[i].upper())