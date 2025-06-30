'''Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''
jogador = dict()
gol = list()
jogador['Jogador'] = str(input('Nome do jogador: '))
Partida = int(input(f'Quantas partidas {jogador["Jogador"]} jogou? '))
for partidas in range (0, Partida):
    jogador['Gols'] = int(input(f'Quantos gols na partida {partidas+1}º: '))
    gol.append(jogador['Gols'])
jogador['Total'] =  sum(gol)
jogador['Gols'] = gol
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador['Jogador']} jogou {Partida} partidas. ')
for partidas in range (0, Partida):
    print(f'    => Na partida {partidas+1}º, fez {jogador['Gols'][partidas]} gols.')
print(f'Foi um total de {jogador['Total']} Gols.')