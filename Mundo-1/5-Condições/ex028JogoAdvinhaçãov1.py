import random
from time import sleep
print('Vou pensar em um numero entre 0 e 5 Tente advinhar!')
sleep(1)
print('PROCESSANDO...')
sleep(1)
a = random.randint(0,5) # computador 'pensa' em um numero
num = int(input('Escolha um numero entre 0 e 5: ')) # usuario tenta adivinhar
if a == num:
    print('Você venceu!')
else:
    print(f'Você perdeu, pensei no numero {a}!')
