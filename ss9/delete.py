item = ['blue','red','green','teal']

print("Our  list: ", *item)

p = input("Ban muon xoa mau theo so hay chu: ")

if p == 'so':
    s = int(input("Mau ban muon xoa: "))
    item.pop(s)
    print("Our new list: ", *item)
elif p == 'chu':
    c = str(input("Chu ban muon xoa"))
    item.remove(c)
    print("Our new list: ", *item)
