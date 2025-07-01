'''Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''
from time import sleep
jogadores = []
jogador = {}
gol = []
while True:
    jogador.clear()
    gol.clear()
    jogador['Jogador'] = str(input('Nome do jogador: ')).capitalize()
    Partida = int(input(f'Quantas partidas {jogador["Jogador"]} jogou? '))
    for partidas in range (0, Partida):
        gols_partida = int(input(f'Quantos gols na partida {partidas+1}º: '))
        gol.append(gols_partida)
    jogador['Gols'] = gol[:]
    jogador['Total'] =  sum(gol)
    jogadores.append(jogador.copy())
    go = ' '
    while go not in 'SN':
        go = input('Quer continuar? [S/N]: ').upper().strip()
    if 'N' in go:
        break
print('-='*30)
print(f'{'Cod':<4}{'Jodares':<10}{'Gols':<20}{'Total':<5}')
for i, v in enumerate(jogadores):
    print(f" {i:<4}{v['Jogador']:<10}{str(v['Gols']):<20}{v['Total']:<5}")
while True:
    print('-='*30)
    busca = int(input('Mostrar dados de qual jogador? [999 Para parar]: '))
    if busca <= (len(jogadores)):
        print('-'*40)
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[busca]['Jogador']}')    
        for i, g in enumerate(jogadores[busca]['Gols']):
            print(f'    => Na partida {i+1}º, fez {g} gols.')
    elif busca >=(len(jogadores)):
        print(f'ERRO! Não existe jogador com o codigo {busca}!')
    if busca == 999:
        print(' FINALIZANDO...')
        sleep(1)
        break
print('<<< VOLTE SEMPRE! >>>')