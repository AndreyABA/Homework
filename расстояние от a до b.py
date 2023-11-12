import math
h=[]
for i in range(4):
    h.append(int(input('Введите координату ')))
a=(h[1]-h[0])**2
b=(h[3]-h[2])**2
print('Расстояние от a до b равно', math.sqrt(a+b))