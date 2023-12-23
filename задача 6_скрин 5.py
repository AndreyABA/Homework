def all_eq(lst):
    a = max(lst, key=lambda x: len(x))
    b = len(a)
    return [item.ljust(b, '_') for item in lst]
print(all_eq(['c', 'cл', 'сло', 'слов', 'слово']))