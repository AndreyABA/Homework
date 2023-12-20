import re
a='56, 91, 503, 327'
a=re.sub('[,]', '', a)
a=a.split()
a=[int(i) for i in a]
print('Сумма объёмов коробок равна', sum(a))