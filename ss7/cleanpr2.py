fav = ['phim', 'nhac', 'truyen']
print(*fav, sep = '|')
new_fav = input("Nhap thu ban thich: ")

fav.append(new_fav)

print(*fav, sep = '|')