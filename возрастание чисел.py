a=[1,5,45,12,48]
c=len(a)
l=1
for i in range(c):
    if a[i-1]!=None:
        if a[i-1]<a[i]:
            l=l+1
if l==c:
    print('Числа в массиве возрастают')
else:
    print('Числа в массиве не возрастают')