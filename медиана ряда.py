a=[1,4,6,8,9,91,53,7,10]
c=len(a)
a=sorted(a)
print(a)
if c%2==0:
    c=c//2
    f=(a[c]+a[c-1])/2
    print('Медиана ряда-', f)
else:
    a.remove(a[0])
    g=len(a)//2
    print('Медиана ряда-',a[g-1])