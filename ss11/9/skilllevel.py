c1 = ['Name: Tackle','Minimum level: 1','Damage: 5','Hit rate: 0.3']
c2 = ['Name: Quick attack','Minimum level: 2','Damage: 3','Hit rate: 0.5']
c3 = ['Name: Strong Kick','Minimum level: 4','Damage: 9','Hit rate: 0.2']
a = 0
print('Skill 1:')
for i in c1: 
    a+=1
    print(a,' ',i)
print('Skill 2:')
b = 0
for i in c2:
    b+= 1
    print(b,' ',i)
c = 0
print('Skill 3:')
for i in c3:
    c+=1
    print(c,' ',i)
chieu = int(input('Chon chieu: '))
level = int(input('Nhap vao level cua ban: '))
if level ==1:
    if chieu == 1:
        print("Su dung thanh cong")
    elif chieu != 1:
        print("Khong the su dung")
elif 0< level <4:
    if chieu == 3:
        print("Khong the su dung chieu")
    else:
        print('Su dung thanh cong')
elif level >4:
    print("Su dung thanh cong")

