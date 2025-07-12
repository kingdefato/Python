'''Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer.
 Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.'''
from time import sleep


def ajuda(com):
    título(f'Acessando o manual do comando {com}',)
    help(com.lower())
    sleep(2)


def título(msg, ):
    tam = len(msg)+4
    print('~' * tam)
    print(f'  {msg}  ')
    print('~' * tam)
    sleep(1)


# Programa Principal
comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP',)
    comando = str(input('Função ou Biblioteca: '))
    if comando.upper() == 'FIM':
        título('ATE LOGO!', )
        break
    else:
        ajuda(comando)
