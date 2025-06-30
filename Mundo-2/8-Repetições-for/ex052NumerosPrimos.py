num = int(input('Digite um numero: '))
ca = 0
total = 0
for c in range(1,num+1):
    if num%c == 0:
        print('\033[1;33m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[mO numero {num} foi divisível {total} vezes.')
if total == 2:
    print(f'Portanto o numero {num} É PRIMO.')
else:
    print(f'Portanto o {num} NÃO É PRIMO.')