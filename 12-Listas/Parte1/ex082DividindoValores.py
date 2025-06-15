listanum = []
pares = []
impares = []
while True:
    n = int(input('Digite um valor: '))
    listanum.append(n)
    if n%2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    go = ' '
    while go not in 'SN':
        go = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if 'N' in go:
        break
'''for i, v in enumerate(n):
    if n % 2 == 0:
        pares.append(n)
    elif n % 2 == 1:
        impares.append(n)'''
print(f'Valores Informados: {listanum}')
print(f'Valores Pares: {pares}')
print(f'Valores Ímpares: {impares}')