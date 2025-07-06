from time import sleep
def maior(*num):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    print(f'Foram informados {len(num)} valores ao todo.')
    for valor in num:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'O maior valor é {maior}.')


valores = []
while True:
    num = int(input('Digite um número: '))
    valores.append(num)
    go = input('Quer continuar? [S/N]: ').strip().upper()[0]
    while go not in 'SN':
        go = input('Quer continuar? [S/N]: ').strip().upper()[0]
    if go == 'N':
        break

maior(*valores)
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6, 8, 3, 2, 5, 9)
maior()