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
m = input("Loai may ban chon la: ")
sl = int(input("So luong ban muon: "))
print("Gia cua", sl, "may",m,'la: ',int(n[m]*sl))