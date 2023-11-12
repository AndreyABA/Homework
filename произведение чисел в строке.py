import math
import re
a='2, 8, 6, 2'
a=re.sub('[,]', '', a)
a=a.split()
a=[int(i) for i in a]
print('Произведение чисел в строке равно', math.prod(a))