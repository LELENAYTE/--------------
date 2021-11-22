from dz31 import vvodspiska


def sred_arifm(b):
    resultat = sum(b) / len(b)
    return resultat


b = [float(item) for item in vvodspiska()]
print(sred_arifm(b))
