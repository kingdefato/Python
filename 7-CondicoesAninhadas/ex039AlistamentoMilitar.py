from datetime import date
anoatual = date.today().year
print('Qual seu sexo:')
print('''Escolha uma das opções abaixo
[ 1 ] Para \033[4mMASCULINO\033[m
[ 2 ] Para \033[4mFEMININO\033[m''')
opção = int(input('Sua opção: '))

if opção == 1:
    nascimento = int(input('Ano de nascimento: '))
    Idade = anoatual - nascimento
    alistamento = 18
    print('Você tem a obrigação de se alistar para o exercito.')
    print(
        f'Quem nasceu no ano de {nascimento} tem {Idade} Anos em {anoatual}.')
    if Idade > alistamento:
        print(
        f'Seu alistamento foi em {nascimento+alistamento}, Você deveria ter se alistado a {Idade-alistamento} Ano(s).')
    elif Idade < alistamento:
        print(
        f'Seu alistamento sera em {nascimento+alistamento}, Você deve se alistar em {alistamento-Idade} Ano(s).')
    else:
        print(
        'Seu alistamento sera esse ano, você deve se alistar \033[1;31mIMEDIATAMENTE!\033[m')
elif opção == 2:
    print('Você não precisa se alistar ao exercito.')
else: 
    print('\033[1;31mOpção invalida! Tente Novamente.\033[m')
