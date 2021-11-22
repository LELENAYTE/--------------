def vvodspiska():
    b = list()  # создали список b
    x = input()  # вводим элементы списка
    while x != "":  # проверка на пустую строку
        b.append(x)
        x = input()
    return b

if __name__ == "__main__":
    print(vvodspiska())
    
