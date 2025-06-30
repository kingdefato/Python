from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('''Escolha uma das opções para jogar:
      [0] Para PEDRA
      [1] Para PAPEL
      [2] Para TESOURA''')
jogador = int(input('Sua escolha:'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
sleep(1)
print('-='*10)
print(f'O Computador escolheu {itens[computador]}')
print(f'O Jogador escolheu {itens[jogador]}')
print('-='*10)
if computador == 0: # Computador jogou PEDRA
    if computador == jogador:
        print('\033[1;33mHOUVE UM EMPATE!\033[m')
    elif jogador == 1:
        print('\033[1;32mO JOGADOR GANHOU!\033[m')
    elif jogador == 2:
        print('\033[1;31mO JOGADOR PERDEU!\033[m')
    else:
        print('\033[1;31mJogada invalida! Tente Novamente.\033[m')    
elif computador == 1: # Computador jogou PAPEL
    if computador == jogador:
        print('\033[1;33mHOUVE UM EMPATE!\033[m')
    elif jogador == 2:
        print('\033[1;32mO JOGADOR GANHOU!\033[m')
    elif jogador == 0:
        print('\033[1;31mO JOGADOR PERDEU!\033[m')
    else:
        print('\033[1;31mJogada invalida! Tente Novamente.\033[m')    
elif computador == 2: # Computador jogou TESOURA
    if computador == jogador:
        print('\033[1;33mHOUVE UM EMPATE!\033[m')
    elif jogador == 0:
        print('\033[1;32mO JOGADOR GANHOU!\033[m')
    elif jogador == 1:
        print('\033[1;31mO JOGADOR PERDEU!\033[m')
    else:
        print('\033[1;31mJogada invalida! Tente Novamente.\033[m')
