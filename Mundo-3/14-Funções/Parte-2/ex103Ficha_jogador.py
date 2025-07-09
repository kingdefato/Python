def ficha(nome='<desconhecido>', gols=0):
    print('-'*45)
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')


# Programa Principal
jogador = input('Nome do jogador: ')
gol = input('Numero de gols: ')
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if jogador.strip() == '':
    ficha(gols=gol)
else:
    ficha(jogador, gol)
