m = {
    'HP': 20,
    'DELL': 50,
    'MACBOOK': 12,
    'ASUS':  30,
}

m['MACBOOK'] = 2
m['DELL'] += 10
m['TOSHIBA'] = 10
m['FUJITSU'] = 15
m['ALIENWARE'] = 5
print(m)


n = {
    'HP': 600,
    'DELL': 650,
    'MACBOOK': 12000,
    'ASUS': 400,
    'ACER': 350,
    'TOSHIBA': 600,

    'FUJITSU': 900,

    'ALIENWARE': 1000,
}
print(n)
count = 0
for key in m:
    tm = int(m[key])*int(n[key])
    count += tm

    print("Gia cua tat ca may",key,"la",n[key]*m[key])
print("Tong gia tri tat ca loai may: ",count)