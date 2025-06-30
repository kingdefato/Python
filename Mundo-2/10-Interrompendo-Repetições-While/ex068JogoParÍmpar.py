from random import randint
print('=-'*30)
print('VAMOS JOGAR PAR OU íMPAR')
print('=-'*30)
Vitórias = 0
par = False
impar = False
while True:
    computador = randint(1 , 10)
    jogador = int(input('Digite um valor: '))
    impopar = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    total = computador + jogador
    print('-'*60)
    print(f'Você jogou {jogador} e o computador {computador}. Total foi {total}', end='')
    if total%2 == 0:
        print(' PAR')
        print('-'*60)
        par = True
        if 'Pp' in impopar:
            Vitórias += 1
            print('Você VENCEU!\nVamos jogar novamente...')
        else:
            print('Você PERDEU!')
            break
    else:
        print(' ÍMPAR')
        print('-'*60)
        impar = True
        if 'Ii' in impopar:
            Vitórias += 1
            print('Você VENCEU!\nVamos jogar novamente...')
        else:
            print('Você PERDEU!')
            break
  