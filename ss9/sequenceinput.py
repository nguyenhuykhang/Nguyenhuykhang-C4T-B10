n = int(input("Enter a number: "))
n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))
n3 = int(input("Enter a number: "))
n4 = int(input("Enter a number: "))
n5 = int(input("Enter a number: "))

l = [n, n1, n2 ,n3, n4, n5]
print("Our list: ", *l,sep = ', ')

for i in l:
    if i%2 ==0:
        print(i)