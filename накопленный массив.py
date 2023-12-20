a=[1,5,7,12,48]
g=[]
c=len(a)
b=0
for i in range(c):
    if a[i-1]!=None:
        b=b+a[i]
        g.append(b)
print(g)