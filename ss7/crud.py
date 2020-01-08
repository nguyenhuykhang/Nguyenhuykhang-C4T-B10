items = ['pho','bun','chao','com', 'mien']
while True:
    n = str(input("Chon mot chu cai C, R, U, D: "))

    if n == 'C' :
        t = input("Nhap thu ban thich: ")
        items.append(t)
        print(items)
    elif n == 'R':
        
        if len(items) == 0:
            print("Khong co gia tri trong danh sach")
        else:
            for i in items:
                print(i)

    elif n == 'U':
        v = int(input('Vi tri ban muon thay doi :'))
        items[v] = input("Thu ban muon thay doi: ")
        print(items)

    elif n == 'D':
        vt = int(input('Vi tri ban muon xoa: '))
        items.pop(vt)
        print(items)


                