from random import randint
def sorteador(*num):
    print(f'Sorteando {len(num)} valores da lista:', end=' ')
    for n in num:
        print(f'{n}', end=' ')
    print()

def soma_pares(*num):
    par = 0
    for n in num:
        if n % 2 == 0:
            par += n
    print(f'Somando os valores pares de {sorteio}, temos {par}.')
quant = 0
while quant < 1 or quant > 10:
    quant = int(input('Quantos números você quer sortear? [MAX = 10]: '))
    if quant < 1 or quant > 10:
        print(f'\033[1;31mERRO! {quant} não está entre 1 e 10. Tente Novamente.\033[m')
sorteio = []
for c in range(0, quant):
    num = randint(1, 10)
    sorteio.append(num)

sorteador(*sorteio)
soma_pares(*sorteio)