# Exercicio 98 - Função Contador
# Crie um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem. Seu programa tem que realizar três contagens através da função criada:
# a) De 1 até 10, de 1 em 1.
# b) De 10 até 0, de 2 em 2.
# c) Uma contagem personalizada.
from time import sleep

def mostralinha():
    print('-=' * 20)


mostralinha()
print('Contagem de 1 até 10 pulando de 1 em 1:')
for c in range(1, 11, 1):
    print(f'{c}', end=' ', flush=True)
    sleep(0.5)
print('FIM!')
mostralinha()

print('Contagem de 10 até 2 pulando de 2 em 2:')
for c in range(10, -1, -2):
    print(f'{c}', end=' ', flush=True)
    sleep(0.5)
print('FIM!')
mostralinha()
def contador(inicio, fim, passo):
    
    if passo < 0:
        passo *= -1

    if passo == 0:
        passo = 1

    print(f'Contagem de {inicio} até {fim} pulando de {passo} em {passo}:')
    for c in range(inicio, fim, passo):
        print(f'{c}', end=' ', flush=True)
        sleep(0.5)
    print('FIM!')



print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
mostralinha()
contador(inicio, fim, passo)
mostralinha()
print('<<< FIM DO PROGRAMA >>>')