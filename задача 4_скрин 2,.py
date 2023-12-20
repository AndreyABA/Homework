def to_dict(lst):
    return {key: key for key in lst}
list1 = ["Почему", "так", "Сложно?"]
a = to_dict(list1)
print(a)