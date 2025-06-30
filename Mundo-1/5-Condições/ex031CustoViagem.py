num = int(input('informe a distancia percorrida em km/h: '))
if num<=200:
    preço = num*0.5
else:
    preço = num*0.45
print(f'O valor da passagem sera R${preço:.2f}')
    