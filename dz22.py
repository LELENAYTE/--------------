vvod = input("Введите строку: ")
# print(vvod)
k = int(input("Введите число k: "))
schetchik = 0
for i in vvod:
    if i.isdigit():
        schetchik += 1
        if schetchik == k:
            print(str(k) + "-я цифра в строке:\t" + str(i))
            break
