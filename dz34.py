from dz31 import vvod

def proverka(your_list, kolvo):
    for i in your_list:
        if i in kolvo:
            kolvo[i] += 1
        else:
            kolvo[i] = 1
    return your_list, kolvo


lst = []
kolvo = {}
proverka(vvod(lst), kolvo)
print("Элемент | Частота")
for b in kolvo:
    print("'%s'|\t%d" % (b, kolvo[b]))
