def season(num):
    if num == 12 or 1 <= num <= 2:
        sezon = "Зима"
    elif 3 <= num <= 5:
        sezon = "Весна"
    elif 6 <= num <= 8:
        sezon = "Лето"
    elif 9 <= num <= 11:
        sezon = "Осень"
    else:
        sezon = "Неверно введён номер месяца!"
    return sezon


n = int(input("Введите номер месяца (1-12): "))
print(season(n))
