import random
def game(player, pc):
    if player==pc:
        return 'ничья'
    elif (player=='камень' and pc=='ножницы') or \
        (player=="ножницы" and pc=='бумага') or \
        (player=='бумага' and pc=='камень'):
        return 'ты победил'
    else:
        return 'ты проиграл'
zxc=['камень', 'ножницы', 'бумага']
choice=input('выбери камень, ножницы или бумага: ')
while choice not in zxc:
    print('с читами нельзя')
    choice=input('выбери камень, ножницы или бумага: ')
choice2=random.choice(zxc)
print(f'ты - {choice}, компьютер - {choice2}.')
print(game(choice, choice2))