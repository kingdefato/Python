
print('='*40)
print(f'{'BANCO YTALLO': ^40}')
print('='*40)
saque = int(input('Qual valor deseja sacar: R$'))
total = saque
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('='*40)
print('Volte Sempre ao BANCO YTALLO! Tenha um bom dia!')