a=[]
c=int(input('Сколько карт? '))
for i in range(c):
    a.append(int(input('Введите достоинсвто карты ')))
a=sum(a)
if a<=21:
    print('False')
if a>21:
    print('True')