items = ['pho','bun','chao']
for i in range(3):
    fav = input("Nhap vao thu ban muon them: ")
    items.append(fav)
# = len(items)
#for i in enumerate range(l):

   # print(items[i], '.')

for i, item in enumerate(items):
    print(i, '.',item)
