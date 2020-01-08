may = {
    'HP': '20',
    'DELL': '50',
    'MACBOOK': '12',
    'ASUS':  '30',
}
may['TOSHIBA'] = 10
n = input("Loai may ban muon them: ")
m = input("So luong ban muon: ")
may[n]= m
print(may)