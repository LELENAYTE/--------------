from dz31 import vvodspiska


def sred_arifm(b):
    return sum(b) / len(b)

b = [float(item) for item in vvodspiska()]
print(sred_arifm(b))
