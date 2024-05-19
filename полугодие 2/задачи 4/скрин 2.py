import collections
import re
def func(a):
    with open(a, 'r') as file:
        text=file.read().lower()
        slova=re.findall(r'\b\w+\b', text)
        return collections.Counter(slova).most_common()
print(func('screen3text.txt'))  