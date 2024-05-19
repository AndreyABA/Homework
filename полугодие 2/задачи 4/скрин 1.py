from itertools import permutations
def func(slovo):
    length=len(slovo)
    b=[]
    for i in range(1, length + 1):
        b.extend([''.join(p) for p in permutations(slovo, i)])
    return b
slovo='негр'
print(func(slovo))
