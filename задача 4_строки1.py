def camel(st):
    a=''
    b=0
    for index, c in enumerate(st):
        if c.isalpha():
            if b%2==0:
                a+=c.upper()
            else:
                a+=c.lower()
            b+=1
        else:
            a+=c
    return a
print(camel('Текст с чередующимся регистром'))