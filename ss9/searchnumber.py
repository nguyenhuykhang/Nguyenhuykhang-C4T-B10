l = [5, 1, 8, 92, -1,30]

n = int(input("Enter a number: "))

if n in l:
    print("Found", "position: ", l.index(n))
else:
    print("Not Found")