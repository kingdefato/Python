import random
from time import sleep
print('Vou pensar em um numero entre 0 e 10 Tente advinhar!')
sleep(1)
print('PROCESSANDO...')
sleep(1)
computador = random.randint(0,10) # computador 'pensa' em um numero
print('Sera que você consegue advinhar qual foi?')
palpites = 0
acertou = False
while not acertou:
    jogador = int(input('Qual é seu palpite? ')) # usuario tenta adivinhar
    if jogador == computador:
        palpites += 1
        acertou = True
        print(f'Você acertou com {palpites} tentativas, Parabéns!')
    else: 
        if computador > jogador:
            print('Mais... Tente mais uma vez. ')
        else:
            print('Menos... Tente mais uma vez.')
