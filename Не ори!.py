import re
a='Ты здесь!!!!!'
if '?' in a:
    a=re.sub('[?]', '', a)
    a+='?'
if '!' in a:
    a=re.sub('[!]', '', a)
    a+='!'
print(a)