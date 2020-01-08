m = {
    'HP': 20,
    'DELL': 50,
    'MACBOOK': 12,
    'ASUS':  30,
}
print(m)
m['TOSHIBA'] = 10
m['FUJITSU'] = 15
m['ALIENWARE'] = 5

for key, value in sorted(m.items()):
   print(key,': ', value)
print('Tong so may: ',sum(m.values()))

