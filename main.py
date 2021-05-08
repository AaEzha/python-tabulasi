angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
row = []
x = 1

print("{:<3} ".format('-'), end='')
for i in angka:
    print("{:<3} ".format(i), end='')

print("")

for i in angka:
    col = []
    for y in angka:
        col.append(i + y)
    row.append(col)

for i in row:
    print("{:<3} ".format(x), end='')
    for j in i:
        print("{:<3} ".format(j), end='')
    x += 1
    print("")
