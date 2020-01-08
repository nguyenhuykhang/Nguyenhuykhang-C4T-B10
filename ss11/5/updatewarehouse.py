m = {
    'HP': 20,
    'DELL': 50,
    'MACBOOK': 12,
    'ASUS':  30,
}
print(m)
m['MACBOOK'] = 2
m['DELL'] += 10
m['TOSHIBA'] = 10
m['FUJITSU'] = 15
m['ALIENWARE'] = 5
print(m)

may = input("Loai may ban muon mua: ")
may = may.upper()
sl = int(input("So luong ban muon mua: "))
if (sl > m[may]):
    print("khong du so luong may")
else:
    cl = int(m[may]) - sl
    print("So may",may,'con lai la:',cl) 
