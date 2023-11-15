a=int(input('Сколько букв будет в вашем слове '))
b=[]
for i in range(a):
    b.append(input('Нажмите клавишу нужное кол-во раз '))
b=([len(r) for r in b])
c=len(b)
for r in range(c):
    b[r]=b[r]+1071
for u in range(c):
    b[u]=chr(b[u])
print(''.join(b))