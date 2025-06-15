pessoas = list()
leves = list()
pesados = list()
cadastrogeral = list()
ncadastros = 0
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))
    cadastrogeral.append(pessoas[:])
    pessoas.clear()
    ncadastros += 1
    go = ' '
    while go not in 'SN':
        go = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if 'N' in go:
        break
for p in cadastrogeral:
    if p[1] >100:
        pesados.append(p[0])
    elif p[1] <70:
        leves.append(p[0])
print(f'{ncadastros} Pessoas foram cadastradas. ')
print(f'As pessoas com os maiores pesos são: {pesados}\nE as com menor peso são: {leves}')
