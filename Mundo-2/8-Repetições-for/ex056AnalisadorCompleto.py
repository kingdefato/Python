somaidade = 0
maioridade = 0
nomevelho = ''
totmulher20 = 0
for c in range (1,5):
    print('='*20,f'{c}º PESSOA', '='*20)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    print('''Escolha uma das opções abaixo:
          Digite [ M ] Para \033[4mMASCULINO\033[m
          Digite [ F ] Para \033[4mFEMININO\033[m''')
    sexo = str(input('Sua opção: ')).strip()
    somaidade += idade
    mediaidade = somaidade/4
    if c == 1  and sexo in'Mm':
            maioridade = idade
            nomevelho = nome
    if sexo in 'Mm' and idade > maioridade:
            maioridade = idade
            nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20+= 1
print(f'A media de idade do grupo é de {int(mediaidade)} Anos')
print(f'O homem mais velho tem {maioridade} Anos e se chama {nomevelho}')
print(f'E {totmulher20} Mulheres tem menos de 20 anos.')
