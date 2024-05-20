def func(i):
    if i<=1:
        return False
    if i<=3:
        return True
    if i%2==0 or i%3==0:
        return False
    g=5
    while g*g<=i:
        if i%g==0 or i%(g+2)==0:
            return False
        g+=6
    return True
a=int(input('введите начало интервала: '))
b=int(input('введите конец интервала: '))
c=sum(i for i in range(a, b + 1) if func(i))
print(c)