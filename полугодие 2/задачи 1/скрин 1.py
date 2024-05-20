text=input('введите строку: ')
slova=text.lower().split()
slova=[''.join(a for a in word if a.isalnum()) for word in slova]
slova2=sorted(set(slova))
print('уникальные слова: ')
for word in slova2:
    print(word)