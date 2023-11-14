import re
a='язык хакера'
a=re.sub('[а]', '4', a)
a=re.sub('[е]', '3', a)
print(a)