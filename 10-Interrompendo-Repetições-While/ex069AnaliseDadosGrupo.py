c = 1
idade18 = homens = mulheres20 = 0
while True:
    print('='*35)
    print(f'CADASTRE A {c}º PESSOA')
    print('='*35)
    idade = int(input(f'Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input(f'Qual sexo? [M/F]: ')).strip().upper()[0]
    print('='*35)
    c += 1
    if idade >= 18:
        idade18 += 1
    if 'M' in sexo:
        homens +=1
    if 'F' in sexo and idade <20:
        mulheres20 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if 'N' in continuar:
        break
print(f'{idade18} Pessoas tem mais de 18 anos de idade.')
print(f'{homens} Homens foram cadastrados.')
print(f'{mulheres20} Mulheres com menos de 20 anos foram cadastradas.')