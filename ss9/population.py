quan = ['ST', 'BĐ', 'BTL', 'CG', 'DD', 'HBT']

count = 0
dientich =['117.43', '9.224', '43.35', '12.04', '9.96', '10.09']
danso = ['150.300', '247.100', '333.300', '266.800', '420.900', '318.000']

for i in quan:
  count += 1
  print(count, ' ',i)
print("Thu tu dien tich quan  ung voi thu tu cac quan: ")
c = 0
for ii in dientich:

   c += 1
   print(c,' ',ii)
print("Thu tu dan so quan: ")
t = 0
for iii in danso:
  t += 1
  print(t,' ',iii)

u = 0 
print("Mat do dan cu cac quan theo thu tu la: ")
for e in range(6):
    u += 1
    md = float(float(danso[e]) / float(dientich[e]))
    print(u, ' ', md)

   
    
    

