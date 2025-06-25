''' Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar
as notas de cada aluno individualmente.'''
classe = []
while True:
    nomes= str(input('Nome do aluno: '))
    nota1= float(input('Primeira Nota: '))
    nota2= float(input('Segunda Nota: '))
    media = (nota1+nota2) /2
    classe.append([nomes, [nota1, nota2,], media])
    go = ' '
    while go not in 'SN':
        go = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if 'N' in go:
        break 
print('-='*30) 
print(f'{'Nº':<4}{'NOME':<10}{'MEDIA':>8}')
print('-'*30)
for i, c in enumerate(classe):    
    print(f'{i:<4}{c[0]:<10} {c[2]:>8.1f}')
print('-'*30)
while True:
    notas = int(input('Mostrar nota de qual aluno? (999 Iterrompe) '))
    if notas <= len(classe) - 1:
        print(f'As notas de {classe[notas][0]} são {classe[notas][1]}')
        print('-'*30)
    elif notas == 999:
        print('FINALIZANDO...   ')
        break
print('<<< VOLTE SEMPRE! >>>')