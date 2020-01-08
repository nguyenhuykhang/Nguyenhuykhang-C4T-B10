fav = ['phim', 'nhac', 'truyen']
print(*fav)
new_fav = input("Nhap thu ban thich: ")

fav.append(new_fav)

print(*fav, sep = ', ')
