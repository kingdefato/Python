from time import sleep
def maior(*num):
    print('-=' * 30)
    print('Analisando os valores passados...')
    print(f'Foram informados {len(num)} valores ao todo.')
    for n in num:
        print(f'{n}', end=' ')
    print()
    print(f'O maior valor é {max(num)}.')
    sleep(3)

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