c = int(input('Digite um numero para calcular seu fatorial: '))
fatorial = 1
while c > 0:
    print(f'{c} ', end='')
    print(' x ' if c> 1 else ' = ', end='')
    fatorial = fatorial*c
    c -= 1
print(f'{fatorial}')