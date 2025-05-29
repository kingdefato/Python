print('-'*40)
print(f'{'LOJA DO YTALLO': ^40}')
print('-'*40)
tot = p1000 = preço= c = menor = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    tot += preço
    c += 1
    if preço > 1000:
        p1000 += 1
    if c == 1 or preço < menor:
        menor = preço
        barato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer Continuar? [S/N]: ')).strip().upper()[0]
    if 'N' in continuar :
        break
print(f'{'FIM DO PROGRAMA':-^40}')
print(f'O Total da compra foi R${tot:.2f}')
print(f'Temos {p1000} produto custando mais que R$1000.00')
print(f'{barato.capitalize()} foi o produto mais barato e custa R${menor:.2f}')