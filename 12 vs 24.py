def password(o):
    l=0
    if len(o) > 7:
        l+=1
    if any(char.isupper() for char in o):
        l+=1
    if any(char.isalnum() == False for char in o):
        l+=1
    if any(char.isdigit() for char in o):
        l+=1
    if any(char.islower() for char in o):
        l+=1
    return l
o = input("Введите пароль: ")
b = password(o)
print(f"Оценка сложности пароля: {b}")