def biggest_dict(**kwargs):
    my_dict = {'first_one': 'we can do it'}
    my_dict.update(kwargs)
    return my_dict
a = biggest_dict(key2='что-то', key3='слово')
print(a)