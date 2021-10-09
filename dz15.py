x = int(input("Введите первое число (X)\t"))
y = int(input("Введите второе число(Y)\t"))
if x > 0 and y < 0:
    print("это 4/4")
elif x > 0 and y > 0:
    print("это 1/4")
elif x < 0 and y > 0:
    print("это 2/4")
elif x < 0 and y < 0:
    print("это 3/4")
elif y == 0:
    print("Точка лежит на оси X")
elif x == 0:
    print ("Точка лежит на оси Y")