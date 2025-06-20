pessoas = list()
cadastrogeral = list()
mai = men = 0
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))
    if len(cadastrogeral) == 0:
        mai = men = pessoas[1]
    else:
        if pessoas[1] > mai:
            mai = pessoas[1]
        if pessoas[1] < men:
            men = pessoas[1]
    cadastrogeral.append(pessoas[:])
    pessoas.clear()
    go = ' '
    while go not in 'SN':
        go = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if 'N' in go:
        break
print(f'{len(cadastrogeral)} Pessoas foram cadastradas. ')
print(f'O maior peso foi de {mai}Kg. Peso de ', end= '')
for p in cadastrogeral:        
    if p[1] == mai:
        print(f'[{p[0]}] ', end= '')
print()
print(f'O menor peso foi de {men}Kg. Peso de ', end= '')
for p in cadastrogeral:
    if p[1] == men:
        print(f'[{p[0]}] ', end= '')
print()