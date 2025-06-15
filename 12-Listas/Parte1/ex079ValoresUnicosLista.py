listanum = []
while True:
    n = int(input('Digite um valor: '))
    if n not in listanum:
        listanum.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print(f'Esse valor ja existe, portanto sera ignorado.')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer Continuar? [S/N]: ')).strip().upper()[0]
    if 'N' in continuar:
        break
listanum.sort()
print('=-'*20)    
print(f'O valores adicionados foram:\n {listanum}')