def sred_arifm(b):
    resultat = 0.0
    summa = sum(b)
    resultat = summa / len(b)
    return resultat


from dz31 import vvodspiska
b = [float(item) for item in vvodspiska()]
print(sred_arifm(b))
