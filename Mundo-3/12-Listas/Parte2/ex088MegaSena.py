'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''
from random import randint
from time import sleep
jogos = []
mega = []
print('-'*60)
print(f'{'JOGA NA MEGA SENA!':^60}')
print('-'*60)
jogadas = int(input('\033[1;34mQuantos jogos você quer jogar? \033[m'))
print('-'*60)
print('-='*3,' SORTEANDO JOGADAS ','=-'*3)
for c in range(1, jogadas+1):
    for c in range(1, 7):
        mega_sena = randint(1, 60)
        jogos.append(mega_sena)
    jogos.sort()
    mega.append(jogos[:])
    jogos.clear()
for c in range(0, jogadas):
    print(f'Jogo {c+1}: {mega[c]}')
    sleep(0.4)
print('-='*5, ' < \033[1;32mBOA SORTE\033[m > ', '=-' *5)