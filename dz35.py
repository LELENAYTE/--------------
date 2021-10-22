def sred_arifm(b):
    resultat = 0.0
    summa = 0.0
    for i in range(len(b)):
        summa = summa + float(b[i])
    resultat = summa / len(b)
    return resultat


b = list()
print("Введите значения: \t")
x = input()
while x != "":
    b.append(float(x))
    x = input()
print(float(sred_arifm(b)))
