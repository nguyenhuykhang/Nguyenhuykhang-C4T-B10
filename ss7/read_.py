fav = ['phim', 'nhac', 'truyen']
print(*fav)
new_fav = input("Nhap thu ban thich: ")

fav.append(new_fav)

print(*fav)

print(fav[0])
print(fav[-1])
print(fav[-2])