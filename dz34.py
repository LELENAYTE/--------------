def vvod(lst):
    b = list()  # создали список b
    print("Введите элементы списка")
    x = input()  # вводим элементы списка
    while x != "":  # проверка на пустую строку
        b.append(x)
        x = input()
    return b


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
