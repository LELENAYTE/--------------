spisok = input()
left = spisok.count('(')
right = spisok.count(')')
proverka = left - right
if proverka > 0:
    print('Не хватает закрывающих:', proverka)
elif proverka < 0:
    print('Не хватает открывающих:', -proverka)
else:
    print('Ошибок нет')
