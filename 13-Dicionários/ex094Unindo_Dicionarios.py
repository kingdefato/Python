'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
 No final, mostre: 
 A) Quantas pessoas foram cadastradas 
 B) A média de idade 
 C) Uma lista com as mulheres 
 D) Uma lista de pessoas com idade acima da média'''
cadastrados = []
cadastro = {}
soma_idades = 0
while True:
    cadastro.clear()
    cadastro['Nome'] = input('Nome: ')
    cadastro['sex'] = input('Sexo: [M/F]: ').strip().upper()[0]
    while cadastro['sex'] not in 'MF':
        print('ERRO! Por favor digite apenas M ou F.')
        cadastro['sex'] = input('Sexo: [M/F]: ').strip().upper()[0]
    cadastro['idade'] = int(input('Idade: '))
    soma_idades += cadastro['idade']
    cadastrados.append(cadastro.copy())
    go = input('Quer continuar? [S/N]: ').strip().upper()[0]
    while go not in 'SN':
        print('ERRO! Por favor digite apenas S ou N.')
        go = input('Quer continuar? [S/N]: ').strip().upper()[0]
    if 'N' in go:
        break
media = soma_idades / len(cadastrados)
print(f'A) Quantas pessoas foram cadastradas:  {len(cadastrados)}')
print(f'B) A média de idade: {media}')
print(f'C) Uma lista com as mulheres foram:', end=' ')
for p in cadastrados:
    if p['sex'] == 'F':
        print(f'{p['Nome']}', end=' ')
    print()
print(f'D) Uma lista de pessoas com idade acima da média: ', end=' ')
for p in cadastrados:
    if p['idade'] >= media:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}', end='')
        print()
print('<< ENCERRADO >>')