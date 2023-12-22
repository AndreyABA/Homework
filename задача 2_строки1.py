def first_last(letter, st):
    a=None
    b=None
    for i in range(len(st)):
        if st[i]==letter:
            if a is None:
                a=i
            b=i
    return (a, b)
letter='c'
st='cdfhoisdhcnvueoquytc'
print(first_last(letter, st))
