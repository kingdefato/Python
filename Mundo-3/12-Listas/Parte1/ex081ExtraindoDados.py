lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    go = ' '
    while go not in 'SN':
        go = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if 'N' in go:
        break
print('-='*30)
print(f'{len(lista)} Valores foram informados.')
lista.sort(reverse=True)
print(f'Lista organizada de forma decrescente {lista}')
if 5 in lista:
    print('O valor 5 foi encontrado na lista!')
else:
    print('O valor 5 não foi encontrado na lista!')