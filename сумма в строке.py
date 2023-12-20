a="UHc1iQ10sU1"
def summa_chisel(b):
    c=0
    t=0
    for i in b:
        if i.isdigit():
            c=c*10 + int(i)
        else:
            t+=c
            c=0
    t+=c
    return t
r=summa_chisel(a)
print("Сумма чисел в строке равна", r)