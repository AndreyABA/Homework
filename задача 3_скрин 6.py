sequence='1111144455'
def count_it(sequence):
    a={}
    for r in sequence:
        r=int(r)
        a[r]=a.get(r, 0)+1
    b=sorted(a.items(), key=lambda x: x[1], reverse=True)
    g={}
    for i in range(min(3, len(b))):
        g[b[i][0]]=b[i][1]
    return g
print(count_it(sequence))