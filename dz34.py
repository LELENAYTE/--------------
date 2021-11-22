def proverka(your_list, kolvo):
    for i in your_list:
        if i in kolvo:
            kolvo[i] += 1
        else:
            kolvo[i] = 1
    return your_list, kolvo

from dz31 import vvodspiska
lst = []
kolvo = {}
proverka(vvodspiska(), kolvo)
print("Элемент | Частота")
for b in kolvo:
    print("'%s'|\t%d" % (b, kolvo[b]))
