slovar={'слово': 1, 'ааааааа': 2, 'сигма': 3, 'раскольников': 4, 'путин': 5}
a=list(slovar.keys())
b=list(slovar.values())
key1=a[0]
key2=a[-1]
b[0], b[-1]=b[-1], b[0]
slovar2=dict(zip(a, b))
del slovar2[list(slovar2.keys())[1]]
slovar2['new_key']='new_value'
print(slovar2)