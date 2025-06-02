from random import randint
num = (randint(1,10), randint(1,10),  randint(1,10),  randint(1,10),  randint(1,10))
print('O valores sorteados foram:', end=' ')
for n in num:
    print(f'{n}', end=' ')
print(f'\nO maior valor foi {max(num)} e o Menor valor foi {min(num)}')
