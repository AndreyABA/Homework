a=int(input('Введите число от 0 до 999 '))
if a>999:
    print('Введите число от 0 до 999')
def name_number(a):
    edenitsi=['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    desyatki=['десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать',
             'семнадцать', 'восемнадцать', 'девятнадцать']
    desyat=['', '', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    sotni=['', 'сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']
    b=''
    if a//100>0:
        b+=sotni[a // 100]+' '
    remainder = a % 100
    if remainder // 10 == 1:
        b+=desyatki[remainder - 10]+' '
    else:
        b+=desyat[remainder // 10]+' '
        b+=edenitsi[remainder % 10]+' '
    if a==0:
        print('ноль')
    return b.strip()
b = name_number(a)
print(f'{b}')
if a>999:
    print('Введите число от 0 до 999')