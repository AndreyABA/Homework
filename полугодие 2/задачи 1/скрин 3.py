import string
def func(input_string):
    a=''.join(i for i in input_string if i not in string.punctuation).replace(" ", "").lower()
    return a==a[::-1]
text=input('введите строку: ')
if func(text):
    print('палиндромом')
else:
    print('не палиндромом')