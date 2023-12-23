def cleaned_str(st):
    a=[]
    for i in st:
        if i=='@' and a:
            a.pop()
        elif i!='@':
            a.append(i)
    return ''.join(a)
print(cleaned_str('кr@аа@кo@ая-тt@о фраj@за8@'))
