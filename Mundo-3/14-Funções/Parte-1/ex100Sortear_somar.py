from random import randint
from time import sleep


def sorteador(lista):
    print(f'Sorteando {quant} valores da lista:', end=' ')
    for c in range(0, quant):
        num = randint(1, 10)
        lista.append(num)
        print(f'{num}', end=' ', flush=True)
        sleep(0.3)
    print()


def soma_pares(lista):
    par = 0
    for n in lista:
        if n % 2 == 0:
            par += n
    print(f'Somando os valores pares de {lista}, temos {par}.')


quant = 0
while quant < 1 or quant > 10:
    quant = int(input('Quantos números você quer sortear? [MAX = 10]: '))
    if quant < 1 or quant > 10:
        print(
            f'\033[1;31mERRO! {quant} não está entre 1 e 10. Tente Novamente.\033[m')
numeros = []
sorteador(numeros)
soma_pares(numeros)
