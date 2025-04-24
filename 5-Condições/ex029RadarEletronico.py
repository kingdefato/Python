km = int(input('Velocidade do carro em Km/h: '))
if km>80:
    print('Você excedeu o limite de velocidade e foi multado!')
    print(f'Valor a pagar R${(km-80)*7:.2f}')
else:
    print('Velocidade permitida!')