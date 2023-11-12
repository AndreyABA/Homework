a=['х','о','к','к','е','й']
c=len(a)
for i in range(c):
    if a[i]==a[i+1]:
        a.append(0)
    else:
        a.append(1)
if 0 in a:
    print('True')
else:
    print('В слове нет удвоенных букв')