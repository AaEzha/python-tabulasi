angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("{:<3} ".format('-'), end='')
for i in angka:
    print("{:<3} ".format(i), end='')

print("")

for i in angka:
    print("{:<3} ".format(i), end='')
    for y in angka:
        print("{:<3} ".format(i + y), end='')
    print("")
