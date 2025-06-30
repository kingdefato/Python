from time import sleep
n1 = int(input('\033[1mDigite o primeiro Valor: \033[m'))
n2 = int(input('\033[1mDigite o segundo Valor: \033[m'))
opção = 0
while opção != 5:
    print('''
        [ 1 ] \033[1;36mSomar\033[m
        [ 2 ] \033[1;34mMultiplicar\033[m
        [ 3 ] \033[1;35mIdentificar Maior\033[m
        [ 4 ] \033[1;33mNovós Númeors\033[m
        [ 5 ] \033[1;31mSair do Programa\033[m
        ''')
    opção = int(input('\033[1;32mQual sua opção: \033[m'))
    print('==-'*10)
    if opção == 1:
        print(f'A \033[1;36mSOMA\033[m entre {n1} + {n2} é \033[4m{n1+n2}\033[m')
    elif opção == 2:
        print(f'A \033[1;34mMULTIPLICAÇÃO\033[m entre {n1} x {n2} é \033[4m{n1*n2}\033[m')
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'O \033[1;35mMAIOR\033[m valor é \033[4m{maior}\033[m')
    elif opção == 4:
        print('Informe os \033[1;33mNOVOS NÚMEROS\033[m.')
        n1 = int(input('Primeiro Valor: '))
        n2 = int(input('Segundo Valor: '))
    elif opção == 5:
        print('\033[1mFinalizando....\033[m')
    else:
        print('\033[1;31mOpção Invalida!\033[m')
    print('==-'*10)
    sleep(1.5)
print('\033[1;33mPrograma Encerrado! Volte Sempre.\033[m')