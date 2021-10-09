a = int(input("Введите первое целое число (a)\t"))
b = int(input("Введите второе целое число (b)\t"))
c = int(input("Введите третье целое число (c)\t"))
d = int(input("Введите четвертое целое число (d)\t"))
f = int(input("Введите пятое целое число (f)\t"))
razn = f - d
if razn == 0:
    print ("Делить на 0 нельзя!")
else:
    print((a * b - c) / razn )
