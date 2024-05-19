def func(a, b):
    if b==0:
        return 1
    else:
        return a * func(a, b-1)
print(func(4, 6))